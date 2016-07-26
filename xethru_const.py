# Constants for the XeThru Serial Protocol

# Protocol flags
XETHRU_START = 0x7d
XETHRU_END = 0x7e
XETHRU_ESC = 0x7f

# Defined values
XTS_DEF_PINGVAL = 0xeeaaeaae
XTS_DEF_PONGVAL_READY = 0xaaeeaeea
XTS_DEF_PONGVAL_NOTREADY = 0xaeeaeeaa

# Application identifiers
XTS_ID_APP_RESP = 0x1423a2d6
XTS_ID_APP_PRESENCE = 0x00288912
XTS_ID_APP_SLEEP = 0x00f17b17

# Status identifiers
XTS_ID_RESP_STATUS = 0x2375fe26
XTS_ID_PRESENCE_STATUS = 0x991a52be
XTS_ID_SLEEP_STATUS = 0x2375a16c

# Generic identifiers
XTS_ID_DETECTION_ZONE = 0x96a10a1c
XTS_ID_SENSITIVITY = 0x10a5112b

# Baseband output identifiers
XTS_ID_BASEBAND_IQ = 0x0C
XTS_ID_BASEBAND_AMPLITUDE_PHASE = 0x0D
XTS_SACR_OUTPUTBASEBAND = 0x10
XTS_SACR_ID_BASEBAND_OUTPUT_OFF = 0x00
XTS_SACR_ID_BASEBAND_OUTPUT_IQ = 0x01
XTS_SACR_ID_BASEBAND_OUTPUT_AMPLITUDE_PHASE = 0x02

# Command codes
XTS_SPC_PING = 0x01
XTS_SPC_APPCOMMAND = 0x10
XTS_SPC_MOD_SETMODE = 0x20
XTS_SPC_MOD_LOADAPP = 0x21
XTS_SPC_MOD_RESET = 0x22

XTS_SPC_MOD_SETLEDCONTROL = 0x24

XTS_SPC_DIR_COMMAND = 0x90

XTS_SPCA_SET = 0x10

XT_UI_LED_MODE_OFF = 0
XT_UI_LED_MODE_SIMPLE = 1
XT_UI_LED_MODE_FULL = 2

XTS_SM_RUN = 0x01
XTS_SM_IDLE = 0x11

XTS_SDC_APP_SETINT = 0x71

# Response codes
XTS_SPR_PONG = 0x01
XTS_SPR_ACK = 0x10
XTS_SPR_ERROR = 0x20
XTS_SPR_SYSTEM = 0x30
XTS_SPR_APPDATA = 0x50
XTS_SPRS_BOOTING = 0x10
XTS_SPRS_READY = 0x11

# Range limits
XETHRU_RESP_MIN = 0.5
XETHRU_RESP_MAX = 2.5
XETHRU_RESP_SPAN_MIN = 0.2
XETHRU_RESP_SPAN_MAX = 0.7

XETHRU_PRES_MIN = 0.5
XETHRU_PRES_MAX = 4.5
XETHRU_PRES_SPAN_MIN = 0.8
XETHRU_PRES_SPAN_MAX = 2.8

XETHRU_SLEEP_MIN = 0.4
XETHRU_SLEEP_MAX = 2.5
XETHRU_SLEEP_SPAN_MIN = 0.2
XETHRU_SLEEP_SPAN_MAX = 1.6

# Respiration application codes
XTS_VAL_RESP_STATE_BREATHING = 0
XTS_VAL_RESP_STATE_MOVEMENT = 1
XTS_VAL_RESP_STATE_MOVEMENT_TRACKING = 2
XTS_VAL_RESP_STATE_NO_MOVEMENT = 3
XTS_VAL_RESP_STATE_INTIALIZING = 4
XTS_VAL_RESP_STATE_RESERVED = 5
XTS_VAL_RESP_STATE_UNKNOWN = 6