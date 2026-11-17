"""The Tuya BLE integration."""
from __future__ import annotations
from dataclasses import dataclass

from enum import StrEnum
from tuya_iot import TuyaCloudOpenAPIEndpoint
from typing_extensions import Final

DOMAIN: Final = "tuya_ble_plus"

DEVICE_METADATA_UUIDS: Final = "uuids"

DEVICE_DEF_MANUFACTURER: Final = "Tuya"
SET_DISCONNECTED_DELAY = 10 * 60

CONF_UUID: Final = "uuid"
CONF_LOCAL_KEY: Final = "local_key"
CONF_CATEGORY: Final = "category"
CONF_PRODUCT_ID: Final = "product_id"
CONF_DEVICE_NAME: Final = "device_name"
CONF_PRODUCT_MODEL: Final = "product_model"
CONF_PRODUCT_NAME: Final = "product_name"
CONF_FUNCTIONS: Final = "functions"
CONF_STATUS_RANGE: Final = "status_range"

CONF_AUTH_TYPE: Final = "auth_type"
CONF_PROJECT_TYPE: Final = "tuya_project_type"
CONF_ENDPOINT: Final = "endpoint"
CONF_ACCESS_ID: Final = "access_id"
CONF_ACCESS_SECRET: Final = "access_secret"
CONF_APP_TYPE: Final = "tuya_app_type"
TUYA_RESPONSE_CODE: Final = "code"
TUYA_RESPONSE_RESULT: Final = "result"
TUYA_RESPONSE_MSG: Final = "msg"
TUYA_RESPONSE_SUCCESS: Final = "success"

# Smart Life / Tuya Smart QR code login (same as Home Assistant's official Tuya
# integration, backed by the tuya_sharing (tuya-device-sharing-sdk) library).
CONF_USER_CODE: Final = "user_code"
CONF_TOKEN_INFO: Final = "token_info"
CONF_TERMINAL_ID: Final = "terminal_id"
CONF_SHARING_DEVICE: Final = "sharing_device"
TUYA_CLIENT_ID: Final = "HA_3y9q4ak7g4ephrvke"
TUYA_SCHEMA: Final = "haauthorize"
TUYA_RESPONSE_QR_CODE: Final = "qrcode"
TUYA_QR_LOGIN_URL: Final = "tuyaSmart--qrLogin?token=%s"
QR_FIELD: Final = "QR"
LOGIN_METHOD_QR: Final = "qr"
LOGIN_METHOD_IOT: Final = "iot"
SHARING_TOKEN_KEYS: Final = ("t", "uid", "expire_time", "access_token", "refresh_token")

TUYA_DOMAIN: Final = "tuya"

SMARTLIFE_APP = "smartlife"
TUYA_SMART_APP = "tuyaSmart"

TUYA_API_DEVICES_URL: Final = "/v1.0/users/%s/devices"
TUYA_API_FACTORY_INFO_URL: Final = "/v1.0/iot-03/devices/factory-infos?device_ids=%s"
TUYA_API_DEVICE_SPECIFICATION: Final = "/v1.1/devices/%s/specifications"
TUYA_FACTORY_INFO_MAC: Final = "mac"

BATTERY_STATE_LOW: Final = "low"
BATTERY_STATE_NORMAL: Final = "normal"
BATTERY_STATE_HIGH: Final = "high"

BATTERY_NOT_CHARGING: Final = "not_charging"
BATTERY_CHARGING: Final = "charging"
BATTERY_CHARGED: Final = "charged"

CO2_LEVEL_NORMAL: Final = "normal"
CO2_LEVEL_ALARM: Final = "alarm"

FINGERBOT_MODE_PUSH: Final = "push"
FINGERBOT_MODE_SWITCH: Final = "switch"
FINGERBOT_MODE_PROGRAM: Final = "program"
FINGERBOT_BUTTON_EVENT: Final = "fingerbot_button_pressed"

CONNECTED_DP_ID = -2

@dataclass
class Country:
    """Describe a supported country."""

    name: str
    country_code: str
    endpoint: str = TuyaCloudOpenAPIEndpoint.AMERICA


# https://developer.tuya.com/en/docs/iot/oem-app-data-center-distributed?id=Kafi0ku9l07qb
TUYA_COUNTRIES = [
    Country("Afghanistan", "93", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Albania", "355", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Algeria", "213", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("American Samoa", "1-684", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Andorra", "376", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Angola", "244", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Anguilla", "1-264", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Antarctica", "672", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Antigua and Barbuda", "1-268", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Argentina", "54", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Armenia", "374", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Aruba", "297", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Australia", "61", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Austria", "43", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Azerbaijan", "994", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bahamas", "1-242", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bahrain", "973", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bangladesh", "880", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Barbados", "1-246", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Belarus", "375", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Belgium", "32", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Belize", "501", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Benin", "229", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bermuda", "1-441", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bhutan", "975", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bolivia", "591", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Bosnia and Herzegovina", "387", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Botswana", "267", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Brazil", "55", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("British Indian Ocean Territory", "246", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("British Virgin Islands", "1-284", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Brunei", "673", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Bulgaria", "359", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Burkina Faso", "226", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Burundi", "257", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Cambodia", "855", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Cameroon", "237", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Canada", "1", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Capo Verde", "238", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Cayman Islands", "1-345", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Central African Republic", "236", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Chad", "235", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Chile", "56", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("China", "86", TuyaCloudOpenAPIEndpoint.CHINA),
    Country("Christmas Island", "61"),
    Country("Cocos Islands", "61"),
    Country("Colombia", "57", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Comoros", "269", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Cook Islands", "682", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Costa Rica", "506", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Croatia", "385", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Cuba", "53"),
    Country("Curacao", "599", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Cyprus", "357", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Czech Republic", "420", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Democratic Republic of the Congo", "243", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Denmark", "45", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Djibouti", "253", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Dominica", "1-767", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Dominican Republic", "1-809", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("East Timor", "670", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Ecuador", "593", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Egypt", "20", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("El Salvador", "503", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Equatorial Guinea", "240", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Eritrea", "291", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Estonia", "372", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Ethiopia", "251", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Falkland Islands", "500", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Faroe Islands", "298", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Fiji", "679", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Finland", "358", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("France", "33", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("French Polynesia", "689", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Gabon", "241", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Gambia", "220", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Georgia", "995", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Germany", "49", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Ghana", "233", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Gibraltar", "350", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Greece", "30", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Greenland", "299", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Grenada", "1-473", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Guam", "1-671", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Guatemala", "502", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Guernsey", "44-1481"),
    Country("Guinea", "224"),
    Country("Guinea-Bissau", "245", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Guyana", "592", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Haiti", "509", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Honduras", "504", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Hong Kong", "852", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Hungary", "36", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Iceland", "354", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("India", "91", TuyaCloudOpenAPIEndpoint.INDIA),
    Country("Indonesia", "62", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Iran", "98"),
    Country("Iraq", "964", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Ireland", "353", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Isle of Man", "44-1624"),
    Country("Israel", "972", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Italy", "39", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Ivory Coast", "225", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Jamaica", "1-876", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Japan", "81", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Jersey", "44-1534"),
    Country("Jordan", "962", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Kazakhstan", "7", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Kenya", "254", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Kiribati", "686", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Kosovo", "383"),
    Country("Kuwait", "965", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Kyrgyzstan", "996", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Laos", "856", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Latvia", "371", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Lebanon", "961", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Lesotho", "266", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Liberia", "231", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Libya", "218", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Liechtenstein", "423", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Lithuania", "370", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Luxembourg", "352", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Macao", "853", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Macedonia", "389", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Madagascar", "261", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Malawi", "265", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Malaysia", "60", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Maldives", "960", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mali", "223", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Malta", "356", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Marshall Islands", "692", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mauritania", "222", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mauritius", "230", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mayotte", "262", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mexico", "52", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Micronesia", "691", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Moldova", "373", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Monaco", "377", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mongolia", "976", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Montenegro", "382", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Montserrat", "1-664", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Morocco", "212", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Mozambique", "258", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Myanmar", "95", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Namibia", "264", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Nauru", "674", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Nepal", "977", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Netherlands", "31", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Netherlands Antilles", "599"),
    Country("New Caledonia", "687", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("New Zealand", "64", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Nicaragua", "505", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Niger", "227", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Nigeria", "234", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Niue", "683", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("North Korea", "850"),
    Country("Northern Mariana Islands", "1-670", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Norway", "47", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Oman", "968", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Pakistan", "92", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Palau", "680", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Palestine", "970", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Panama", "507", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Papua New Guinea", "675", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Paraguay", "595", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Peru", "51", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Philippines", "63", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Pitcairn", "64"),
    Country("Poland", "48", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Portugal", "351", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Puerto Rico", "1-787, 1-939", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Qatar", "974", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Republic of the Congo", "242", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Reunion", "262", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Romania", "40", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Russia", "7", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Rwanda", "250", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Barthelemy", "590", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Helena", "290"),
    Country("Saint Kitts and Nevis", "1-869", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Lucia", "1-758", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Martin", "590", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Pierre and Miquelon", "508", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country(
        "Saint Vincent and the Grenadines", "1-784", TuyaCloudOpenAPIEndpoint.EUROPE
    ),
    Country("Samoa", "685", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("San Marino", "378", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sao Tome and Principe", "239", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Saudi Arabia", "966", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Senegal", "221", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Serbia", "381", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Seychelles", "248", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sierra Leone", "232", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Singapore", "65", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sint Maarten", "1-721", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Slovakia", "421", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Slovenia", "386", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Solomon Islands", "677", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Somalia", "252", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("South Africa", "27", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("South Korea", "82", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("South Sudan", "211"),
    Country("Spain", "34", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sri Lanka", "94", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sudan", "249"),
    Country("Suriname", "597", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Svalbard and Jan Mayen", "4779", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Swaziland", "268", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Sweden", "46", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Switzerland", "41", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Syria", "963"),
    Country("Taiwan", "886", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Tajikistan", "992", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Tanzania", "255", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Thailand", "66", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Togo", "228", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Tokelau", "690", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Tonga", "676", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Trinidad and Tobago", "1-868", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Tunisia", "216", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Turkey", "90", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Turkmenistan", "993", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Turks and Caicos Islands", "1-649", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Tuvalu", "688", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("U.S. Virgin Islands", "1-340", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Uganda", "256", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Ukraine", "380", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("United Arab Emirates", "971", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("United Kingdom", "44", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("United States", "1", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Uruguay", "598", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Uzbekistan", "998", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Vanuatu", "678", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Vatican", "379", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Venezuela", "58", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Vietnam", "84", TuyaCloudOpenAPIEndpoint.AMERICA),
    Country("Wallis and Futuna", "681", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Western Sahara", "212", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Yemen", "967", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Zambia", "260", TuyaCloudOpenAPIEndpoint.EUROPE),
    Country("Zimbabwe", "263", TuyaCloudOpenAPIEndpoint.EUROPE),
]


class WorkMode(StrEnum):
    """Work modes."""

    COLOUR = "colour"
    MUSIC = "music"
    SCENE = "scene"
    WHITE = "white"


class DPType(StrEnum):
    """Data point types."""

    BOOLEAN = "Boolean"
    ENUM = "Enum"
    INTEGER = "Integer"
    JSON = "Json"
    RAW = "Raw"
    STRING = "String"


class DPCode(StrEnum):
    """Data Point Codes used by Tuya.

    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
    """

    ADD_ELE = "add_ele"  # energy
    AIR_QUALITY = "air_quality"
    AIR_QUALITY_INDEX = "air_quality_index"
    ALARM_DELAY_TIME = "alarm_delay_time"
    ALARM_MESSAGE = "alarm_message"
    ALARM_MSG = "alarm_msg"
    ALARM_STATE = "alarm_state"
    ALARM_SWITCH = "alarm_switch"  # Alarm switch
    ALARM_TIME = "alarm_time"  # Alarm time
    ALARM_VOLUME = "alarm_volume"  # Alarm volume
    ALL_ENERGY = "all_energy"  # Combined energy of all channels
    ANGLE_HORIZONTAL = "angle_horizontal"
    ANGLE_VERTICAL = "angle_vertical"
    ANION = "anion"  # Ionizer unit
    ARM_DOWN_PERCENT = "arm_down_percent"
    ARM_UP_PERCENT = "arm_up_percent"
    ATMOSPHERIC_PRESSTURE = "atmospheric_pressture"  # Typo is in Tuya API
    AUTO_CLEAN = "auto_clean"
    BACKUP_RESERVE = "backup_reserve"
    BASIC_ANTI_FLICKER = "basic_anti_flicker"
    BASIC_DEVICE_VOLUME = "basic_device_volume"
    BASIC_FLIP = "basic_flip"
    BASIC_INDICATOR = "basic_indicator"
    BASIC_NIGHTVISION = "basic_nightvision"
    BASIC_OSD = "basic_osd"
    BASIC_PRIVATE = "basic_private"
    BASIC_WDR = "basic_wdr"
    BATTERY = "battery"  # Used by non-standard contact sensor implementations
    BATTERY_PERCENTAGE = "battery_percentage"  # Battery percentage
    BATTERY_POWER = "battery_power"
    BATTERY_STATE = "battery_state"  # Battery state
    BATTERY_VALUE = "battery_value"  # Battery value
    BRIGHT_CONTROLLER = "bright_controller"
    BRIGHT_STATE = "bright_state"  # Brightness status
    BRIGHT_VALUE = "bright_value"  # Brightness
    BRIGHT_VALUE_1 = "bright_value_1"
    BRIGHT_VALUE_2 = "bright_value_2"
    BRIGHT_VALUE_3 = "bright_value_3"
    BRIGHT_VALUE_V2 = "bright_value_v2"
    BRIGHTNESS_MAX_1 = "brightness_max_1"
    BRIGHTNESS_MAX_2 = "brightness_max_2"
    BRIGHTNESS_MAX_3 = "brightness_max_3"
    BRIGHTNESS_MIN_1 = "brightness_min_1"
    BRIGHTNESS_MIN_2 = "brightness_min_2"
    BRIGHTNESS_MIN_3 = "brightness_min_3"
    C_F = "c_f"  # Temperature unit switching
    CAT_WEIGHT = "cat_weight"
    CH2O_STATE = "ch2o_state"
    CH2O_VALUE = "ch2o_value"
    CH4_SENSOR_STATE = "ch4_sensor_state"
    CH4_SENSOR_VALUE = "ch4_sensor_value"
    CHARGE_CUR_SET = "charge_cur_set"
    CHARGE_ENERGY_ONCE = "charge_energy_once"
    CHARGE_STATE = "charge_state"
    CHILD_LOCK = "child_lock"  # Child lock
    CISTERN = "cistern"
    CLEAN_AREA = "clean_area"
    CLEAN_TIME = "clean_time"
    CLICK_SUSTAIN_TIME = "click_sustain_time"
    CLOSED_OPENED_KIT = "closed_opened_kit"
    CLOUD_RECIPE_NUMBER = "cloud_recipe_number"
    CO_STATE = "co_state"
    CO_STATUS = "co_status"
    CO_VALUE = "co_value"
    CO2_STATE = "co2_state"
    CO2_VALUE = "co2_value"  # CO2 concentration
    COLLECTION_MODE = "collection_mode"
    COLOR_DATA_V2 = "color_data_v2"
    COLOUR_DATA = "colour_data"  # Colored light mode
    COLOUR_DATA_HSV = "colour_data_hsv"  # Colored light mode
    COLOUR_DATA_V2 = "colour_data_v2"  # Colored light mode
    COMPRESSOR_STRENGTH = "compressor_strength"
    CONCENTRATION_SET = "concentration_set"  # Concentration setting
    CONTROL = "control"
    CONTROL_2 = "control_2"
    CONTROL_3 = "control_3"
    CONTROL_BACK = "control_back"
    CONTROL_BACK_MODE = "control_back_mode"
    COOK_TEMPERATURE = "cook_temperature"
    COOK_TEMPERATURE_2 = "cook_temperature_2"
    COOK_TIME = "cook_time"
    COUNTDOWN = "countdown"  # Countdown
    COUNTDOWN_1 = "countdown_1"
    COUNTDOWN_2 = "countdown_2"
    COUNTDOWN_3 = "countdown_3"
    COUNTDOWN_4 = "countdown_4"
    COUNTDOWN_5 = "countdown_5"
    COUNTDOWN_6 = "countdown_6"
    COUNTDOWN_7 = "countdown_7"
    COUNTDOWN_8 = "countdown_8"
    COUNTDOWN_LEFT = "countdown_left"
    COUNTDOWN_SET = "countdown_set"  # Countdown setting
    CRY_DETECTION_SWITCH = "cry_detection_switch"
    CUML_E_EXPORT_OFFGRID1 = "cuml_e_export_offgrid1"
    CUMULATIVE_ENERGY_CHARGED = "cumulative_energy_charged"
    CUMULATIVE_ENERGY_DISCHARGED = "cumulative_energy_discharged"
    CUMULATIVE_ENERGY_GENERATED_PV = "cumulative_energy_generated_pv"
    CUMULATIVE_ENERGY_OUTPUT_INV = "cumulative_energy_output_inv"
    CUP_NUMBER = "cup_number"  # NUmber of cups
    CUR_CURRENT = "cur_current"  # Actual current
    CUR_CURRENT1 = "cur_current1"  # Actual current, channel 1
    CUR_CURRENT2 = "cur_current2"  # Actual current, channel 2
    CUR_NEUTRAL = "cur_neutral"  # Total reverse energy
    CUR_POWER = "cur_power"  # Actual power
    CUR_POWER1 = "cur_power1"  # Actual power, channel 1
    CUR_POWER2 = "cur_power2"  # Actual power, channel 2
    CUR_VOLTAGE = "cur_voltage"  # Actual voltage
    CUR_VOLTAGE1 = "cur_voltage1"  # Actual voltage, channel 1
    CUR_VOLTAGE2 = "cur_voltage2"  # Actual voltage, channel 2
    CURRENT_SOC = "current_soc"
    DECIBEL_SENSITIVITY = "decibel_sensitivity"
    DECIBEL_SWITCH = "decibel_switch"
    DEHUMIDITY_SET_ENUM = "dehumidify_set_enum"
    DEHUMIDITY_SET_VALUE = "dehumidify_set_value"
    DELAY_CLEAN_TIME = "delay_clean_time"
    DELAY_SET = "delay_set"
    DEVICE_RESTART = "device_restart"
    DEVICE_STATE1 = "device_state1"  # Channel 1 monitoring state
    DEVICE_STATE2 = "device_state2"  # Channel 2 monitoring state
    DEW_POINT_TEMP = "dew_point_temp"
    DISINFECTION = "disinfection"
    DO_NOT_DISTURB = "do_not_disturb"
    DOORBELL_PIC = "doorbell_pic"
    DOORCONTACT_STATE = "doorcontact_state"  # Status of door window sensor
    DOORCONTACT_STATE_2 = "doorcontact_state_2"
    DOORCONTACT_STATE_3 = "doorcontact_state_3"
    DUSTER_CLOTH = "duster_cloth"
    EC_CURRENT = "ec_current"
    ECO2 = "eco2"
    EDGE_BRUSH = "edge_brush"
    ELECTRICITY_LEFT = "electricity_left"
    EXCRETION_TIME_DAY = "excretion_time_day"
    EXCRETION_TIMES_DAY = "excretion_times_day"
    EXT_TEMP = "ext_temp"
    FACTORY_RESET = "factory_reset"
    FAN_BEEP = "fan_beep"  # Sound
    FAN_COOL = "fan_cool"  # Cool wind
    FAN_DIRECTION = "fan_direction"  # Fan direction
    FAN_HORIZONTAL = "fan_horizontal"  # Horizontal swing flap angle
    FAN_MODE = "fan_mode"
    FAN_SPEED = "fan_speed"
    FAN_SPEED_ENUM = "fan_speed_enum"  # Speed mode
    FAN_SPEED_PERCENT = "fan_speed_percent"  # Stepless speed
    FAN_SWITCH = "fan_switch"
    FAN_VERTICAL = "fan_vertical"  # Vertical swing flap angle
    FAR_DETECTION = "far_detection"
    FAULT = "fault"
    FEED_REPORT = "feed_report"
    FEED_STATE = "feed_state"
    FEEDIN_POWER_LIMIT_ENABLE = "feedin_power_limit_enable"
    FEELLIKE_TEMP = "feellike_temp"
    FILTER = "filter"
    FILTER_DURATION = "filter_life"  # Filter duration (hours)
    FILTER_LIFE = "filter"  # Filter life (percentage)
    FILTER_RESET = "filter_reset"  # Filter (cartridge) reset
    FLOODLIGHT_LIGHTNESS = "floodlight_lightness"
    FLOODLIGHT_SWITCH = "floodlight_switch"
    FORWARD_ENERGY_TOTAL = "forward_energy_total"
    FROST = "frost"  # Frost protection
    GAS_SENSOR_STATE = "gas_sensor_state"
    GAS_SENSOR_STATUS = "gas_sensor_status"
    GAS_SENSOR_VALUE = "gas_sensor_value"
    HEAT_INDEX = "heat_index"
    HUMIDIFIER = "humidifier"  # Humidification
    HUMIDITY = "humidity"  # Humidity
    HUMIDITY_CURRENT = "humidity_current"  # Current humidity
    HUMIDITY_INDOOR = "humidity_indoor"  # Indoor humidity
    HUMIDITY_OUTDOOR = "humidity_outdoor"  # Outdoor humidity
    HUMIDITY_OUTDOOR_1 = "humidity_outdoor_1"  # Outdoor humidity
    HUMIDITY_OUTDOOR_2 = "humidity_outdoor_2"  # Outdoor humidity
    HUMIDITY_OUTDOOR_3 = "humidity_outdoor_3"  # Outdoor humidity
    HUMIDITY_SET = "humidity_set"  # Humidity setting
    HUMIDITY_VALUE = "humidity_value"  # Humidity
    INSTALLATION_HEIGHT = "installation_height"
    INVERTER_OUTPUT_POWER = "inverter_output_power"
    IPC_AUTO_SIREN = "ipc_auto_siren"
    IPC_BRIGHT = "ipc_bright"
    IPC_CONTRAST = "ipc_contrast"
    IPC_SHARP = "ipc_sharp"
    IPC_WORK_MODE = "ipc_work_mode"
    LED_TYPE_1 = "led_type_1"
    LED_TYPE_2 = "led_type_2"
    LED_TYPE_3 = "led_type_3"
    LEVEL = "level"
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_CURRENT = "level_current"
    LIGHT = "light"  # Light
    LIGHT_MODE = "light_mode"
    LIQUID_DEPTH = "liquid_depth"
    LIQUID_DEPTH_MAX = "liquid_depth_max"
    LIQUID_LEVEL_PERCENT = "liquid_level_percent"
    LIQUID_STATE = "liquid_state"
    LOCK = "lock"  # Lock / Child lock
    MACH_OPERATE = "mach_operate"
    MANUAL_CLEAN = "manual_clean"
    MANUAL_FEED = "manual_feed"
    MASTER_MODE = "master_mode"  # alarm mode
    MASTER_STATE = "master_state"  # alarm state
    MATERIAL = "material"  # Material
    MAX_SET = "max_set"
    MINI_SET = "mini_set"
    MODE = "mode"  # Working mode / Mode
    MOODLIGHTING = "moodlighting"  # Mood light
    MOTION_AREA_SWITCH = "motion_area_switch"  # Activity area
    MOTION_RECORD = "motion_record"
    MOTION_SENSITIVITY = "motion_sensitivity"
    MOTION_SWITCH = "motion_switch"  # Motion switch
    MOTION_TRACKING = "motion_tracking"
    MOVEMENT_DETECT_PIC = "movement_detect_pic"
    MUFFLING = "muffling"  # Muffling
    NEAR_DETECTION = "near_detection"
    OPPOSITE = "opposite"
    ORP_CURRENT = "orp_current"
    OUTPUT_POWER_LIMIT = "output_power_limit"
    OXYGEN = "oxygen"  # Oxygen bar
    PAUSE = "pause"
    PERCENT_CONTROL = "percent_control"
    PERCENT_CONTROL_2 = "percent_control_2"
    PERCENT_CONTROL_3 = "percent_control_3"
    PERCENT_STATE = "percent_state"
    PERCENT_STATE_2 = "percent_state_2"
    PERCENT_STATE_3 = "percent_state_3"
    PHASE_A = "phase_a"
    PHASE_B = "phase_b"
    PHASE_C = "phase_c"
    PHASE_S1 = "phase_s1"
    PHASE_S2 = "phase_s2"
    PHASE_S3 = "phase_s3"
    PHASE_S4 = "phase_s4"
    PHASE_S5 = "phase_s5"
    PHASE_S6 = "phase_s6"
    PHASE_S7 = "phase_s7"
    PHASE_S8 = "phase_s8"
    PHASE_S9 = "phase_s9"
    PHASE_S10 = "phase_s10"
    PHASE_S11 = "phase_s11"
    PHASE_S12 = "phase_s12"
    PHASE_S13 = "phase_s13"
    PHASE_S14 = "phase_s14"
    PHASE_S15 = "phase_s15"
    PHASE_S16 = "phase_s16"
    PHASE_S17 = "phase_s17"
    PHASE_S18 = "phase_s18"
    PHASE_S19 = "phase_s19"
    PHASE_S20 = "phase_s20"
    PH_CURRENT = "ph_current"
    PIR = "pir"  # Motion sensor
    PM1 = "pm1"
    PM10 = "pm10"
    PM25 = "pm25"
    PM25_STATE = "pm25_state"
    PM25_VALUE = "pm25_value"
    POSITION = "position"
    POWDER_SET = "powder_set"  # Powder
    POWER = "power"
    POWER_GO = "power_go"
    POWER_TOTAL = "power_total"
    PREHEAT = "preheat"
    PREHEAT_1 = "preheat_1"
    PREHEAT_2 = "preheat_2"
    PRESENCE_STATE = "presence_state"
    PRESSURE_STATE = "pressure_state"
    PRESSURE_VALUE = "pressure_value"
    PRO_ADD_ELE = "pro_add_ele"  # Produce energy
    PUMP = "pump"
    PUMP_RESET = "pump_reset"  # Water pump reset
    PUMP_TIME = "pump_time"  # Water pump duration
    PV_POWER_CHANNEL_1 = "pv_power_channel_1"
    PV_POWER_CHANNEL_2 = "pv_power_channel_2"
    PV_POWER_TOTAL = "pv_power_total"
    RAIN_24H = "rain_24h"  # Total daily rainfall in mm
    RAIN_RATE = "rain_rate"  # Rain intensity in mm/h
    RECORD_MODE = "record_mode"
    RECORD_SWITCH = "record_switch"  # Recording switch
    RELAY_STATUS = "relay_status"
    REMAIN_TIME = "remain_time"
    RESET_DUSTER_CLOTH = "reset_duster_cloth"
    RESET_EDGE_BRUSH = "reset_edge_brush"
    RESET_FILTER = "reset_filter"
    RESET_MAP = "reset_map"
    RESET_ROLL_BRUSH = "reset_roll_brush"
    REVERSE_ENERGY_TOTAL = "reverse_energy_total"
    ROLL_BRUSH = "roll_brush"
    SEEK = "seek"
    SENSITIVITY = "sensitivity"  # Sensitivity
    SENSOR_HUMIDITY = "sensor_humidity"
    SENSOR_TEMPERATURE = "sensor_temperature"
    SHAKE = "shake"  # Oscillating
    SHOCK_STATE = "shock_state"  # Vibration status
    SIREN_SWITCH = "siren_switch"
    SITUATION_SET = "situation_set"
    SLEEP = "sleep"  # Sleep function
    SLOW_FEED = "slow_feed"
    SMOKE_SENSOR_STATE = "smoke_sensor_state"
    SMOKE_SENSOR_STATUS = "smoke_sensor_status"
    SMOKE_SENSOR_VALUE = "smoke_sensor_value"
    SNOOZE = "snooze"
    SOS = "sos"  # Emergency State
    SOS_STATE = "sos_state"  # Emergency mode
    SPEED = "speed"  # Speed level
    SPEED_CURRENT = "speed_current"
    SPEED_SET = "speed_set"
    SPRAY_MODE = "spray_mode"  # Spraying mode
    START = "start"  # Start
    STATUS = "status"
    STERILIZATION = "sterilization"  # Sterilization
    SUCTION = "suction"
    SUPPLY_FREQUENCY = "supply_frequency"
    SWING = "swing"  # Swing mode
    SWITCH = "switch"  # Switch
    SWITCH_1 = "switch_1"  # Switch 1
    SWITCH_2 = "switch_2"  # Switch 2
    SWITCH_3 = "switch_3"  # Switch 3
    SWITCH_4 = "switch_4"  # Switch 4
    SWITCH_5 = "switch_5"  # Switch 5
    SWITCH_6 = "switch_6"  # Switch 6
    SWITCH_7 = "switch_7"  # Switch 7
    SWITCH_8 = "switch_8"  # Switch 8
    SWITCH_ALARM_LIGHT = "switch_alarm_light"
    SWITCH_ALARM_PROPEL = "switch_alarm_propel"
    SWITCH_ALARM_SOUND = "switch_alarm_sound"
    SWITCH_BACKLIGHT = "switch_backlight"  # Backlight switch
    SWITCH_CHARGE = "switch_charge"
    SWITCH_CONTROLLER = "switch_controller"
    SWITCH_DISTURB = "switch_disturb"
    SWITCH_FAN = "switch_fan"
    SWITCH_HORIZONTAL = "switch_horizontal"  # Horizontal swing flap switch
    SWITCH_KB_SOUND = "switch_kb_sound"
    SWITCH_LED = "switch_led"  # Switch
    SWITCH_LED_1 = "switch_led_1"
    SWITCH_LED_2 = "switch_led_2"
    SWITCH_LED_3 = "switch_led_3"
    SWITCH_MODE1 = "switch_mode1"
    SWITCH_MODE2 = "switch_mode2"
    SWITCH_MODE3 = "switch_mode3"
    SWITCH_MODE4 = "switch_mode4"
    SWITCH_MODE5 = "switch_mode5"
    SWITCH_MODE6 = "switch_mode6"
    SWITCH_MODE7 = "switch_mode7"
    SWITCH_MODE8 = "switch_mode8"
    SWITCH_MODE9 = "switch_mode9"
    SWITCH_MUSIC = "switch_music"
    SWITCH_NIGHT_LIGHT = "switch_night_light"
    SWITCH_SAVE_ENERGY = "switch_save_energy"
    SWITCH_SOUND = "switch_sound"  # Voice switch
    SWITCH_SPRAY = "switch_spray"  # Spraying switch
    SWITCH_USB1 = "switch_usb1"  # USB 1
    SWITCH_USB2 = "switch_usb2"  # USB 2
    SWITCH_USB3 = "switch_usb3"  # USB 3
    SWITCH_USB4 = "switch_usb4"  # USB 4
    SWITCH_USB5 = "switch_usb5"  # USB 5
    SWITCH_USB6 = "switch_usb6"  # USB 6
    SWITCH_VERTICAL = "switch_vertical"  # Vertical swing flap switch
    SWITCH_VOICE = "switch_voice"  # Voice switch
    TARGET_DIS_CLOSEST = "target_dis_closest"  # Closest target distance
    TDS_IN = "tds_in"  # Total dissolved solids
    TEMP = "temp"  # Temperature setting
    TEMP_AROUND = "temp_around"  # Current around (outside) temperature
    TEMP_BOILING_C = "temp_boiling_c"
    TEMP_BOILING_F = "temp_boiling_f"
    TEMP_COILER = "temp_coiler"  # Current coil temperature
    TEMP_CONTROLLER = "temp_controller"
    TEMP_CORRECTION = "temp_correction"
    TEMP_CURRENT = "temp_current"  # Current temperature in °C
    TEMP_CURRENT_2 = "temp_current_2"
    TEMP_CURRENT_EXTERNAL = (
        "temp_current_external"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_1 = (
        "temp_current_external_1"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_2 = (
        "temp_current_external_2"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_3 = (
        "temp_current_external_3"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_F = (
        "temp_current_external_f"  # Current external temperature in Fahrenheit
    )
    TEMP_CURRENT_F = "temp_current_f"  # Current temperature in °F
    TEMP_EFFLUENT = "temp_effluent"  # Current flow temperature
    TEMP_INDOOR = "temp_indoor"  # Indoor temperature in °C
    TEMP_SET = "temp_set"  # Set the temperature in °C
    TEMP_SET_F = "temp_set_f"  # Set the temperature in °F
    TEMP_SETTING_QUICK_C = "temp_setting_quick_c"
    TEMP_UNIT_CONVERT = "temp_unit_convert"  # Temperature unit switching
    TEMP_VALUE = "temp_value"  # Color temperature
    TEMP_VALUE_V2 = "temp_value_v2"
    TEMP_VENTING = "temp_venting"  # Current heat plate temperature
    TEMPER_ALARM = "temper_alarm"  # Tamper alarm
    TIME_TOTAL = "time_total"
    TIME_USE = "time_use"  # Total seconds of irrigation
    TODAY_ACC_ENERGY1 = "today_acc_energy1"  # Energy today, channel 1
    TODAY_ACC_ENERGY2 = "today_acc_energy2"  # Energy today, channel 2
    TOTAL_CLEAN_AREA = "total_clean_area"
    TOTAL_CLEAN_COUNT = "total_clean_count"
    TOTAL_CLEAN_TIME = "total_clean_time"
    TOTAL_ENERGY1 = "total_energy1"  # Total energy, channel 1
    TOTAL_ENERGY2 = "total_energy2"  # Total energy, channel 2
    TOTAL_FORWARD_ENERGY = "total_forward_energy"
    TOTAL_PM = "total_pm"
    TOTAL_POWER = "total_power"
    TOTAL_TIME = "total_time"
    TVOC = "tvoc"
    UP_DOWN = "up_down"
    UPPER_TEMP = "upper_temp"
    UPPER_TEMP_F = "upper_temp_f"
    USE_TIME_ONE = "use_time_one"
    UV = "uv"  # UV sterilization
    UV_INDEX = "uv_index"
    UV_RUNTIME = "uv_runtime"  # UV runtime
    VA_BATTERY = "va_battery"
    VA_HUMIDITY = "va_humidity"
    VA_TEMPERATURE = "va_temperature"
    VALVE_STATE = "valve_state"
    VOC_STATE = "voc_state"
    VOC_VALUE = "voc_value"
    VOICE_SWITCH = "voice_switch"
    VOICE_TIMES = "voice_times"
    VOLUME_SET = "volume_set"
    WARM = "warm"  # Heat preservation
    WARM_TIME = "warm_time"  # Heat preservation time
    WARN_POWER1 = "warn_power1"  # Power warning threshold, channel 1
    WARN_POWER2 = "warn_power2"  # Power warning threshold, channel 2
    WATER = "water"
    WATER_LEVEL = "water_level"
    WATER_ONCE = "water_once"
    WATER_RESET = "water_reset"  # Resetting of water usage days
    WATER_SET = "water_set"  # Water level
    WATER_TIME = "water_time"  # Water usage duration
    WATER_TOTAL = "water_total"
    WATERSENSOR_STATE = "watersensor_state"
    WEATHER_DELAY = "weather_delay"
    WET = "wet"  # Humidification
    WINDOW_CHECK = "window_check"
    WINDOW_STATE = "window_state"
    WINDCHILL_INDEX = "windchill_index"
    WINDSPEED = "windspeed"
    WINDSPEED_AVG = "windspeed_avg"
    WIND_DIRECT = "wind_direct"
    WIRELESS_BATTERYLOCK = "wireless_batterylock"
    WIRELESS_ELECTRICITY = "wireless_electricity"
    WORK_MODE = "work_mode"  # Working mode
    WORK_POWER = "work_power"
    WORK_STATE = "work_state"
    WORK_STATE_E = "work_state_e"
    WORK_TYPE = "work_type"
