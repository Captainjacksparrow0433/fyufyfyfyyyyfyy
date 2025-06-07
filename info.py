import re, time
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = 8470932
API_HASH = "da8c32735fb13224dd71e8a6504f6989"
BOT_TOKEN = "2013704851:AAEW220ozCvYcc0COb2La7CZHcnBkomB5m8"

# Bot settings
WEB_SUPPORT = True
PICS = [
    "https://graph.org/file/01ddfcb1e8203879a63d7.jpg",
    "https://graph.org/file/d69995d9846fd4ad632b8.jpg",
    "https://graph.org/file/a125497b6b85a1d774394.jpg",
    "https://graph.org/file/43d26c54d37f4afb830f7.jpg",
    "https://graph.org/file/60c1adffc7cc2015f771c.jpg",
    "https://graph.org/file/d7b520240b00b7f083a24.jpg",
    "https://graph.org/file/0f336b0402db3f2a20037.jpg",
    "https://graph.org/file/39cc4e15cad4519d8e932.jpg",
    "https://graph.org/file/d59a1108b1ed1c6c6c144.jpg",
    "https://te.legra.ph/file/3a4a79f8d5955e64cbb8e.jpg",
    "https://graph.org/file/d69995d9846fd4ad632b8.jpg"
]
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = 300
ADMINS = [1325579472]
CHANNELS = [-1001630547396]
AUTH_USERS = ADMINS
AUTH_CHANNEL = None
AUTH_GROUPS = None

# MongoDB information
DATABASE_URL = "mongodb+srv://opop:opop1@cluster0.pn8roxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "Cluster0"
FILE_DB_URL = DATABASE_URL
FILE_DB_NAME = DATABASE_NAME
COLLECTION_NAME = "Telegram_files"

# Filters Configuration 
MAX_RIST_BTNS = 10
START_MESSAGE = script.START_TXT
BUTTON_LOCK_TEXT = script.BUTTON_LOCK_TEXT
FORCE_SUB_TEXT = script.FORCE_SUB_TEXT

WELCOM_PIC = ""
WELCOM_TEXT = script.WELCOM_TEXT
PMFILTER = True
G_FILTER = True
BUTTON_LOCK = True
RemoveBG_API = ""

# url shortner
SHORT_URL = None
SHORT_API = None

# Others
IMDB_DELET_TIME = 300
LOG_CHANNEL = -1001655059349
SUPPORT_CHAT = "MKN_BOTZ_DISCUSSION_GROUP"
P_TTI_SHOW_OFF = True
PM_IMDB = True
IMDB = True
SINGLE_BUTTON = True
CUSTOM_FILE_CAPTION = "{file_name}"
BATCH_FILE_CAPTION = None
IMDB_TEMPLATE = script.IMDB_TEMPLATE
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
FILE_STORE_CHANNEL = []
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
