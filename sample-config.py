# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    # APP_ID = int(os.environ.get("APP_ID"))
    # API_HASH = os.environ.get("API_HASH")
    # BOT_TOKEN = os.environ.get("BOT_TOKEN")
    # BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    # LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL"))
    # MONGODB_URL = os.environ.get("MONGODB_URL")
    # GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN")
    APP_ID = 20417642
    API_HASH = "f1db98019a4acd081430ada305f34498"
    BOT_TOKEN = "7824063151:AAFN4RGPyeXdEL42TYNmsvxU8HmT05laZ6Q"  # unzipstuff_bot
    LOGS_CHANNEL = -1002429834992
    BOT_OWNER = 70283385385 #tony_starkish
    MONGODB_URL = "mongodb+srv://shinanygans:Suborbital&030180@cluster0.xvkpd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    GOFILE_TOKEN = "Lnnfcnll71yTgdM71yYCBXgw95DP98EF"
    
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6