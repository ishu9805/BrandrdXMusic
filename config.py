import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = 26692918
API_HASH = "2b239375e141e882a33b59820ce827be"
# ------------------------------------------------------
BOT_TOKEN = "7328208506:AAHmBq17Li7JgzvBGJUsCjAF4R4Bmg3ZiN4"
# -------------------------------------------------------
OWNER_USERNAME = "alone_x_hater"
# --------------------------------------------------------
BOT_USERNAME = "Blade_Music_bot"
# --------------------------------------------------------
MUSIC_BOT_NAME = "BLADE MUSIC BOT"

EVAL = 7378476666
# ---------------------------------------------------------
ASSUSERNAME = "Naruto_X_Hinata"
# ---------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ishu9805/lailamajnu",
)


UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = getenv("SERVER_PLAYLIST_LIMIT", "3000")

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = getenv("DURATION_LIMIT", 16000)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = 7378476666

# -----------------------------------------------------------------
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "blademusic")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-864141f4-144f-4148-b161-12a69706413d")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

#-----------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = "https://t.me/blade_x_community"
SUPPORT_CHAT = "https://t.me/blade_x_support"
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = True
AUTO_LEAVE_ASSISTANT_TIME = 60

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 100))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
#------------------------------------------------------------------




# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQFLb5sAXR867x8cf_Rb8ytuVnw5TktEZubHpSZer7bYkLBzbeUvwl20uPzLmxSlB0xLCFA26qNm0gzyx14s3leF5K3ImQpTSRvVdiiKZqx51c56zbfoyF1hYrkbaLXW5T6QKKnsIvUUegGL5T4NrO9B1uT0yU1Z0bs72wcE0miBQ1zds7nd5YxoPUSaYwSjKb7zEE4TEFm2TeleyNrO2f98vGC5neD_AQpzRS-fuKWaaJg6ZvTMMzBn0BpDAvklL2JaTg0Nj96Zol1ff1Kfuh9vTyy6_dTZ5C3lGlPOcJfV5KwPCuY8ZsX-Fg5xUnSo8Y1Lri1sNCk9QflHetiojMndny1iawAAAAGTeZOKAA"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))



# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
