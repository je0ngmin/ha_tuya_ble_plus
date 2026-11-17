"""Config flow for Tuya BLE integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from tuya_iot import AuthType
from tuya_sharing import CustomerDevice

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    OptionsFlowWithConfigEntry,
)
from homeassistant.components.bluetooth import (
    BluetoothServiceInfoBleak,
    async_discovered_service_info,
)
from homeassistant.const import (
    CONF_ADDRESS,
    CONF_COUNTRY_CODE,
    CONF_PASSWORD,
    CONF_USERNAME,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowHandler, FlowResult
from homeassistant.helpers import selector

from .tuya_ble import SERVICE_UUID, TuyaBLEDeviceCredentials

from .const import (
    DOMAIN,
    CONF_ACCESS_ID,
    CONF_ACCESS_SECRET,
    CONF_AUTH_TYPE,
    CONF_DEVICE_NAME,
    CONF_ENDPOINT,
    CONF_SHARING_DEVICE,
    CONF_UUID,
    CONF_LOCAL_KEY,
    CONF_USER_CODE,
    LOGIN_METHOD_IOT,
    LOGIN_METHOD_QR,
    QR_FIELD,
    SMARTLIFE_APP,
    TUYA_SMART_APP,
    TUYA_COUNTRIES,
    TUYA_QR_LOGIN_URL,
    TUYA_RESPONSE_CODE,
    TUYA_RESPONSE_MSG,
    TUYA_RESPONSE_QR_CODE,
    TUYA_RESPONSE_RESULT,
    TUYA_RESPONSE_SUCCESS,
    CONF_APP_TYPE,
)
from .cloud import (
    HASSTuyaBLEDeviceManager,
    TuyaSharingLogin,
    fetch_sharing_devices,
    normalize_mac,
    sharing_device_credentials,
    sharing_device_label,
    sharing_device_mac,
    sharing_login_data,
)
from .devices import TuyaBLEData, get_device_readable_name

_LOGGER = logging.getLogger(__name__)


async def _try_login(
    manager: HASSTuyaBLEDeviceManager,
    user_input: dict[str, Any],
    errors: dict[str, str],
    placeholders: dict[str, Any],
) -> dict[str, Any] | None:
    response: dict[Any, Any] | None
    data: dict[str, Any]

    country = [
        country
        for country in TUYA_COUNTRIES
        if country.name == user_input[CONF_COUNTRY_CODE]
    ][0]

    data = {
        CONF_ENDPOINT: country.endpoint,
        CONF_AUTH_TYPE: AuthType.CUSTOM,
        CONF_ACCESS_ID: user_input[CONF_ACCESS_ID],
        CONF_ACCESS_SECRET: user_input[CONF_ACCESS_SECRET],
        CONF_USERNAME: user_input[CONF_USERNAME],
        CONF_PASSWORD: user_input[CONF_PASSWORD],
        CONF_COUNTRY_CODE: country.country_code,
    }

    for app_type in (TUYA_SMART_APP, SMARTLIFE_APP, ""):
        data[CONF_APP_TYPE] = app_type
        if app_type == "":
            data[CONF_AUTH_TYPE] = AuthType.CUSTOM
        else:
            data[CONF_AUTH_TYPE] = AuthType.SMART_HOME

        response = await manager._login(data, True)

        if response.get(TUYA_RESPONSE_SUCCESS, False):
            return data

    errors["base"] = "login_error"
    if response:
        placeholders.update(
            {
                TUYA_RESPONSE_CODE: response.get(TUYA_RESPONSE_CODE),
                TUYA_RESPONSE_MSG: response.get(TUYA_RESPONSE_MSG),
            }
        )

    return None


def _show_login_form(
    flow: FlowHandler,
    user_input: dict[str, Any],
    errors: dict[str, str],
    placeholders: dict[str, Any],
) -> FlowResult:
    """Shows the Tuya IOT platform login form."""
    if user_input is not None and user_input.get(CONF_COUNTRY_CODE) is not None:
        for country in TUYA_COUNTRIES:
            if country.country_code == user_input[CONF_COUNTRY_CODE]:
                user_input[CONF_COUNTRY_CODE] = country.name
                break

    def_country_name = None
    country_code = flow.hass.config.country
    if country_code:
        for country in TUYA_COUNTRIES:
            if country.country_code == country_code:
                def_country_name = country.name
                break

    return flow.async_show_form(
        step_id="login",
        data_schema=vol.Schema(
            {
                vol.Required(
                    CONF_COUNTRY_CODE,
                    default=user_input.get(CONF_COUNTRY_CODE, def_country_name),
                ): vol.In(
                    # We don't pass a dict {code:name} because country codes can be duplicate.
                    [country.name for country in TUYA_COUNTRIES]
                ),
                vol.Required(
                    CONF_ACCESS_ID, default=user_input.get(CONF_ACCESS_ID, "")
                ): str,
                vol.Required(
                    CONF_ACCESS_SECRET,
                    default=user_input.get(CONF_ACCESS_SECRET, ""),
                ): str,
                vol.Required(
                    CONF_USERNAME, default=user_input.get(CONF_USERNAME, "")
                ): str,
                vol.Required(
                    CONF_PASSWORD, default=user_input.get(CONF_PASSWORD, "")
                ): str,
            }
        ),
        errors=errors,
        description_placeholders=placeholders,
    )


class TuyaBLEQRCodeLoginFlow:
    """Smart Life / Tuya Smart QR code login steps.

    The steps do not need a Tuya IoT Access ID / Secret: the user code of the
    mobile app and a QR code scan are enough to read the device credentials
    (uuid, local key, DP functions) from the cloud. They are shared by the
    config flow and the options flow, the host flow implements
    ``_async_qr_create_entry`` to store the result.
    """

    hass: HomeAssistant
    _data: dict[str, Any]

    def _async_qr_init(self) -> None:
        """Initialize the QR code login state of the flow."""
        self._qr_login = TuyaSharingLogin()
        self._qr_user_code: str | None = None
        self._qr_token: str | None = None
        self._qr_login_data: dict[str, Any] = {}
        self._qr_devices: dict[str, CustomerDevice] = {}
        self._qr_device_id: str | None = None
        self._qr_last_error: dict[str, Any] = {}

    async def _async_qr_create_entry(self, address: str) -> FlowResult:
        """Store the QR code login result in the host flow."""
        raise NotImplementedError

    # Address already known (Bluetooth discovery, manual MAC entry, options flow)
    @property
    def _qr_known_address(self) -> str | None:
        return None

    async def async_step_qr(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Ask for the user code of the Smart Life / Tuya Smart app."""
        errors: dict[str, str] = {}
        placeholders: dict[str, Any] = {}

        if user_input is not None:
            self._qr_user_code = user_input[CONF_USER_CODE].strip()
            if await self._async_qr_request_code():
                return await self.async_step_qr_scan()

            errors["base"] = "login_error"
            placeholders = {
                TUYA_RESPONSE_CODE: self._qr_last_error.get(TUYA_RESPONSE_CODE),
                TUYA_RESPONSE_MSG: self._qr_last_error.get(
                    TUYA_RESPONSE_MSG, "Unknown error"
                ),
            }
        else:
            user_input = {}

        return self.async_show_form(
            step_id="qr",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_USER_CODE,
                        default=user_input.get(CONF_USER_CODE, self._qr_user_code or ""),
                    ): str,
                }
            ),
            errors=errors,
            description_placeholders=placeholders,
        )

    async def async_step_qr_scan(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Show the QR code and wait until it is scanned in the app."""
        if self._qr_token is None or self._qr_user_code is None:
            return await self.async_step_qr()

        if user_input is None:
            return self._show_qr_scan_form()

        success, info = await self.hass.async_add_executor_job(
            self._qr_login.get_login_result,
            self._qr_token,
            self._qr_user_code,
        )
        if not success:
            # The QR code may have expired: request a new one and show it again.
            await self._async_qr_request_code()
            return self._show_qr_scan_form(
                errors={"base": "login_error"},
                placeholders={
                    TUYA_RESPONSE_CODE: info.get(TUYA_RESPONSE_CODE),
                    TUYA_RESPONSE_MSG: info.get(TUYA_RESPONSE_MSG, "Unknown error"),
                },
            )

        try:
            self._qr_login_data = sharing_login_data(self._qr_user_code, info)
        except KeyError as err:
            _LOGGER.error("Unexpected QR code login result: %s", err)
            await self._async_qr_request_code()
            return self._show_qr_scan_form(
                errors={"base": "login_error"},
                placeholders={
                    TUYA_RESPONSE_CODE: info.get(TUYA_RESPONSE_CODE),
                    TUYA_RESPONSE_MSG: str(err),
                },
            )

        return await self._async_qr_load_devices()

    async def async_step_qr_device(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Pick the cloud device that belongs to the BLE device."""
        if not self._qr_devices:
            return await self.async_step_qr()
        if self._qr_device_id is not None:
            # The account has only one device, there is nothing to pick.
            return await self.async_step_qr_address()

        errors: dict[str, str] = {}
        if user_input is not None:
            device = self._qr_devices.get(user_input.get(CONF_SHARING_DEVICE))
            if device is not None and self._async_qr_select_device(device):
                return await self.async_step_qr_address()
            errors["base"] = "invalid_cloud_device"

        product_names = {
            device_id: sharing_device_label(device)
            for device_id, device in self._qr_devices.items()
        }
        return self.async_show_form(
            step_id="qr_device",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_SHARING_DEVICE,
                        default=next(iter(product_names), None),
                    ): vol.In(product_names),
                }
            ),
            errors=errors,
            description_placeholders={"device_count": len(product_names)},
        )

    async def async_step_qr_address(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Decide how the BLE address of the device is chosen."""
        if self._qr_device_id is None:
            return await self.async_step_qr()

        if (address := self._qr_known_address) is not None:
            return await self._async_qr_create_entry(address)

        discovered = self._async_qr_discovered_devices()
        if not discovered:
            return await self.async_step_qr_manual()

        return self.async_show_menu(
            step_id="qr_address",
            menu_options=["qr_pick", "qr_manual"],
            description_placeholders={
                "device": self._data.get(CONF_DEVICE_NAME) or "",
                "device_count": len(discovered),
            },
        )

    async def async_step_qr_pick(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Pick the discovered BLE device that is the cloud device."""
        discovered = self._async_qr_discovered_devices()
        if not discovered:
            return await self.async_step_qr_manual()

        if user_input is not None and user_input.get(CONF_ADDRESS):
            return await self._async_qr_create_entry(user_input[CONF_ADDRESS])

        def_address = self._qr_suggested_address(discovered)
        return self.async_show_form(
            step_id="qr_pick",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_ADDRESS,
                        default=def_address,
                    ): vol.In(discovered),
                }
            ),
            description_placeholders={"device": self._data.get(CONF_DEVICE_NAME) or ""},
        )

    async def async_step_qr_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Enter the MAC address of the BLE device manually."""
        errors: dict[str, str] = {}

        if user_input is not None:
            address = normalize_mac(user_input.get(CONF_ADDRESS))
            if address:
                return await self._async_qr_create_entry(address)
            errors["base"] = "invalid_mac"

        return self.async_show_form(
            step_id="qr_manual",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_ADDRESS,
                        default=user_input.get(CONF_ADDRESS) if user_input else "",
                    ): str,
                }
            ),
            errors=errors,
            description_placeholders={
                "example_mac": "DC:23:53:55:C0:EE",
                "device": self._data.get(CONF_DEVICE_NAME) or "",
            },
        )

    # Internal helpers

    async def _async_qr_request_code(self) -> bool:
        """Request a new QR code for the current user code."""
        if not self._qr_user_code:
            return False
        response = await self.hass.async_add_executor_job(
            self._qr_login.request_qr_code,
            self._qr_user_code,
        )
        response = response or {}
        self._qr_last_error = response
        if not response.get(TUYA_RESPONSE_SUCCESS, False):
            return False
        result = response.get(TUYA_RESPONSE_RESULT) or {}
        token = result.get(TUYA_RESPONSE_QR_CODE)
        if not token:
            return False
        self._qr_token = token
        return True

    def _show_qr_scan_form(
        self,
        errors: dict[str, str] | None = None,
        placeholders: dict[str, Any] | None = None,
    ) -> FlowResult:
        return self.async_show_form(
            step_id="qr_scan",
            data_schema=vol.Schema(
                {
                    vol.Optional(QR_FIELD): selector.QrCodeSelector(
                        config=selector.QrCodeSelectorConfig(
                            data=TUYA_QR_LOGIN_URL % self._qr_token,
                            scale=5,
                            error_correction_level=selector.QrErrorCorrectionLevel.QUARTILE,
                        )
                    )
                }
            ),
            errors=errors or {},
            description_placeholders=placeholders or {},
        )

    async def _async_qr_load_devices(self) -> FlowResult:
        """Read the devices of the account and continue with the device pick."""
        try:
            devices = await self.hass.async_add_executor_job(
                fetch_sharing_devices, self._qr_login_data
            )
        except Exception as err:  # noqa: BLE001 - report cloud errors in the form
            _LOGGER.error("Failed to read the devices of the Tuya cloud: %s", err)
            return self._show_qr_scan_form(
                errors={"base": "cloud_error"},
            )

        self._qr_devices = {
            device_id: device
            for device in devices
            if (device_id := getattr(device, "id", None))
        }
        if not self._qr_devices:
            return self.async_abort(reason="no_cloud_devices")

        if len(self._qr_devices) == 1:
            device = next(iter(self._qr_devices.values()))
            if not self._async_qr_select_device(device):
                return self.async_abort(reason="invalid_cloud_device")

        return await self.async_step_qr_device()

    def _async_qr_select_device(self, device: CustomerDevice) -> bool:
        """Use the credentials of the picked cloud device."""
        credentials = sharing_device_credentials(device)
        if not credentials.get(CONF_UUID) or not credentials.get(CONF_LOCAL_KEY):
            _LOGGER.debug(
                "Device %s does not expose BLE credentials",
                getattr(device, "id", None),
            )
            return False

        self._qr_device_id = getattr(device, "id", None)
        self._data.update(self._qr_login_data)
        self._data.update(credentials)
        return True

    def _async_qr_discovered_devices(self) -> dict[str, str]:
        """Discovered Tuya BLE devices, as address to readable name."""
        # Only a config flow can tell which addresses are configured already.
        current: set[str] = set()
        if current_addresses := getattr(self, "_async_current_ids", None):
            current = set(current_addresses())

        discovered: dict[str, str] = {}
        for discovery in async_discovered_service_info(self.hass):
            if (
                discovery.address in current
                or discovery.service_data is None
                or SERVICE_UUID not in discovery.service_data
            ):
                continue
            name = discovery.name or discovery.device.name or discovery.address
            discovered[discovery.address] = f"{name} ({discovery.address})"
        return discovered

    def _qr_suggested_address(self, discovered: dict[str, str]) -> str:
        """Best guess of the BLE address of the picked cloud device."""
        for device in self._qr_devices.values():
            if getattr(device, "id", None) == self._qr_device_id:
                if (mac := sharing_device_mac(device)) and mac in discovered:
                    return mac
        return next(iter(discovered))


class TuyaBLEOptionsFlow(OptionsFlowWithConfigEntry, TuyaBLEQRCodeLoginFlow):
    """Handle a Tuya BLE options flow."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        super().__init__(config_entry)
        self._data = {}
        self._async_qr_init()

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        return self.async_show_menu(
            step_id="init",
            menu_options=[LOGIN_METHOD_QR, "login"],
        )

    async def async_step_login(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the Tuya IOT platform login step."""
        errors: dict[str, str] = {}
        placeholders: dict[str, Any] = {}
        credentials: TuyaBLEDeviceCredentials | None = None
        address: str | None = self.config_entry.data.get(CONF_ADDRESS)

        if user_input is not None:
            entry: TuyaBLEData | None = None
            domain_data = self.hass.data.get(DOMAIN)
            if domain_data:
                entry = domain_data.get(self.config_entry.entry_id)
            if entry:
                login_data = await _try_login(
                    entry.manager,
                    user_input,
                    errors,
                    placeholders,
                )
                if login_data:
                    credentials = await entry.manager.get_device_credentials(
                        address, True, True
                    )
                    if credentials:
                        return self.async_create_entry(
                            title=self.config_entry.title,
                            data=entry.manager.data,
                        )
                    else:
                        errors["base"] = "device_not_registered"

        if user_input is None:
            user_input = {}
            user_input.update(self.config_entry.options)

        return _show_login_form(self, user_input, errors, placeholders)

    @property
    def _qr_known_address(self) -> str | None:
        """The address of the device of this config entry."""
        return self.config_entry.data.get(CONF_ADDRESS)

    async def _async_qr_create_entry(self, address: str) -> FlowResult:
        """Update the credentials of the entry with the QR code login."""
        options = dict(self.config_entry.options)
        options.update(self._data)
        options[CONF_ADDRESS] = self.config_entry.data.get(CONF_ADDRESS, address)
        _LOGGER.debug("Updated credentials of %s with the QR code login", address)
        return self.async_create_entry(title=self.config_entry.title, data=options)


class TuyaBLEConfigFlow(TuyaBLEQRCodeLoginFlow, ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tuya BLE."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        super().__init__()
        self._discovery_info: BluetoothServiceInfoBleak | None = None
        self._discovered_devices: dict[str, BluetoothServiceInfoBleak] = {}
        self._data: dict[str, Any] = {}
        self._manager: HASSTuyaBLEDeviceManager | None = None
        self._get_device_info_error = False
        self._manual_address: str | None = None
        self._async_qr_init()

    async def async_step_bluetooth(
        self, discovery_info: BluetoothServiceInfoBleak
    ) -> FlowResult:
        """Handle the bluetooth discovery step."""
        await self.async_set_unique_id(discovery_info.address)
        self._abort_if_unique_id_configured()
        self._discovery_info = discovery_info
        if self._manager is None:
            self._manager = HASSTuyaBLEDeviceManager(self.hass, self._data)
        await self._manager.build_cache()
        self.context["title_placeholders"] = {
            "name": await get_device_readable_name(
                discovery_info,
                self._manager,
            )
        }
        return await self.async_step_cloud_method()

    async def async_step_cloud_method(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Choose how the device credentials are read from the cloud."""
        return self.async_show_menu(
            step_id="cloud_method",
            menu_options=[LOGIN_METHOD_QR, LOGIN_METHOD_IOT],
        )

    async def async_step_iot(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Use the Tuya IoT platform account."""
        return await self.async_step_login()

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the user step to choose between discovery and manual entry."""
        if self._manager is None:
            self._manager = HASSTuyaBLEDeviceManager(self.hass, self._data)
        await self._manager.build_cache()

        return self.async_show_menu(
            step_id="user",
            menu_options=[LOGIN_METHOD_QR, "discover", "manual"],
        )

    async def async_step_discover(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle automatic discovery."""
        return await self.async_step_login()

    async def async_step_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle manual MAC address entry."""
        errors: dict[str, str] = {}

        if user_input is not None:
            address = user_input[CONF_ADDRESS].upper().strip()
            # Validate MAC address format
            if len(address.replace(":", "").replace("-", "")) == 12:
                # Normalize to colon-separated format
                address_clean = address.replace(":", "").replace("-", "")
                self._manual_address = ":".join(
                    address_clean[i : i + 2] for i in range(0, 12, 2)
                )
                await self.async_set_unique_id(self._manual_address)
                self._abort_if_unique_id_configured()
                return await self.async_step_login()
            else:
                errors["base"] = "invalid_mac"

        return self.async_show_form(
            step_id="manual",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_ADDRESS): str,
                }
            ),
            errors=errors,
            description_placeholders={"example_mac": "DC:23:51:5E:23:CB"},
        )

    async def async_step_login(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the Tuya IOT platform login step."""
        data: dict[str, Any] | None = None
        errors: dict[str, str] = {}
        placeholders: dict[str, Any] = {}

        if self._manager is None:
            self._manager = HASSTuyaBLEDeviceManager(self.hass, self._data)

        if user_input is not None:
            data = await _try_login(
                self._manager,
                user_input,
                errors,
                placeholders,
            )
            if data:
                self._data.update(data)
                return await self.async_step_device()

        if user_input is None:
            user_input = {}
            if self._discovery_info:
                await self._manager.get_device_credentials(
                    self._discovery_info.address,
                    False,
                    True,
                )
            if self._data is None or len(self._data) == 0:
                self._manager.get_login_from_cache()
            if self._data is not None and len(self._data) > 0:
                user_input.update(self._data)

        return _show_login_form(self, user_input, errors, placeholders)

    async def async_step_device(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the user step to pick discovered device."""
        errors: dict[str, str] = {}

        # Handle manual address entry - skip discovery and go straight to credential check
        if self._manual_address:
            address = self._manual_address
            credentials = await self._manager.get_device_credentials(
                address, self._get_device_info_error, True
            )
            self._data[CONF_ADDRESS] = address
            if credentials is None:
                self._get_device_info_error = True
                # Show error but allow retry with same address
                return self.async_show_form(
                    step_id="manual_confirm",
                    data_schema=vol.Schema({}),
                    errors={"base": "device_not_registered"},
                    description_placeholders={"address": address},
                )
            else:
                local_name = f"{credentials.device_name} {address[-8:].replace(':', '')}"
                return self.async_create_entry(
                    title=local_name,
                    data={CONF_ADDRESS: address},
                    options=self._data,
                )

        if user_input is not None:
            address = user_input[CONF_ADDRESS]
            discovery_info = self._discovered_devices[address]
            local_name = await get_device_readable_name(discovery_info, self._manager)
            await self.async_set_unique_id(
                discovery_info.address, raise_on_progress=False
            )
            self._abort_if_unique_id_configured()
            credentials = await self._manager.get_device_credentials(
                discovery_info.address, self._get_device_info_error, True
            )
            self._data[CONF_ADDRESS] = discovery_info.address
            if credentials is None:
                self._get_device_info_error = True
                errors["base"] = "device_not_registered"
            else:
                return self.async_create_entry(
                    title=local_name,
                    data={CONF_ADDRESS: discovery_info.address},
                    options=self._data,
                )

        if discovery := self._discovery_info:
            self._discovered_devices[discovery.address] = discovery
        else:
            current_addresses = self._async_current_ids()
            for discovery in async_discovered_service_info(self.hass):
                if (
                    discovery.address in current_addresses
                    or discovery.address in self._discovered_devices
                    or discovery.service_data is None
                    or not SERVICE_UUID in discovery.service_data.keys()
                ):
                    continue
                self._discovered_devices[discovery.address] = discovery

        if not self._discovered_devices:
            return self.async_abort(reason="no_unconfigured_devices")

        def_address: str
        if user_input:
            def_address = user_input.get(CONF_ADDRESS)
        else:
            def_address = list(self._discovered_devices)[0]

        return self.async_show_form(
            step_id="device",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_ADDRESS,
                        default=def_address,
                    ): vol.In(
                        {
                            service_info.address: await get_device_readable_name(
                                service_info,
                                self._manager,
                            )
                            for service_info in self._discovered_devices.values()
                        }
                    ),
                },
            ),
            errors=errors,
        )

    async def async_step_manual_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle confirmation after manual entry error."""
        if user_input is not None:
            # Retry with force update
            self._get_device_info_error = True
            return await self.async_step_device()

        return self.async_show_form(
            step_id="manual_confirm",
            data_schema=vol.Schema({}),
            description_placeholders={"address": self._manual_address},
        )

    # QR code login

    @property
    def _qr_known_address(self) -> str | None:
        """Address of the device when it is already known."""
        if self._manual_address:
            return self._manual_address
        if self._discovery_info:
            return self._discovery_info.address
        return None

    async def _async_qr_create_entry(self, address: str) -> FlowResult:
        """Create the entry with the credentials read from the cloud."""
        address = address.upper()
        self._data[CONF_ADDRESS] = address
        await self.async_set_unique_id(address, raise_on_progress=False)
        self._abort_if_unique_id_configured()

        device_name = self._data.get(CONF_DEVICE_NAME) or "Tuya BLE"
        title = f"{device_name} {address[-8:].replace(':', '')}"
        _LOGGER.debug(
            "Adding %s with the credentials of the Tuya cloud device %s",
            address,
            self._qr_device_id,
        )
        return self.async_create_entry(
            title=title,
            data={CONF_ADDRESS: address},
            options=self._data,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> TuyaBLEOptionsFlow:
        """Get the options flow for this handler."""
        return TuyaBLEOptionsFlow(config_entry)
