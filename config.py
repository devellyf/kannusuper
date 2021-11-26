from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kannu_op")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kannu_op")
BOT_USERNAME = getenv("BOT_USERNAME")
BG_IMAGE = getenv("BG_IMAGE", " https://telegra.ph/file/141376f69ffcd545ceeec.jpg ")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/141376f69ffcd545ceeec.jpg")
BOT_IMG = getenv("BOT_IMG", " https://telegra.ph/file/141376f69ffcd545ceeec.jpg ")
AUD_IMG = getenv("AUD_IMG", " https://telegra.ph/file/141376f69ffcd545ceeec.jpg ")
QUE_IMG = getenv("QUE_IMG", " https://telegra.ph/file/141376f69ffcd545ceeec.jpg ")

admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

OWNER_ID = int(getenv("OWNER_ID"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
