# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import re

API_ID = "12345678" # Your Telegram API ID
API_HASH = "12345678abcd" # Your Telegram API Hash
BOT_TOKEN = "7267436522:XXXXXXXXXXXXXXXXXX" # Your Bot Token

# MongoDB connection URI
MONGO_URI = "your_mongodb_url"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'('
    r'https?://[^\s]+'              # http/https
    r'|www\.[^\s]+'                 # www.
    r'|t\.me/[^\s]+'                # t.me
    r'|telegram\.me/[^\s]+'         # telegram.me
    r'|@[A-Za-z0-9_]{3,}'           # @username
    r'|[A-Za-z0-9-]+\.[A-Za-z]{2,}' # example.com
    r')',
    re.IGNORECASE
) #done change here
)
