# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import re

API_ID = "38881334" # Your Telegram API ID
API_HASH = "b28ea0d569fb81f8053484a227514135" # Your Telegram API Hash
BOT_TOKEN = "7580042609:AAFR4Xq94hEYLhiw692USJeAHJ9Xf2723Uw" # Your Bot Token

# MongoDB connection URI
MONGO_URI = "mongodb+srv://anshkumariitan2026_db_user:LSqdTj1QxyvZMEYe@cluster0.0zt0rg0.mongodb.net/?appName=Cluster0"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*' #done change here
)
