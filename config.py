# +++ Made By King [telegram username: @Here_remo] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8051853867:AAEnrojX8PODWOE-8i8vnaXHxV7418IcCPo")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002413997036"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "1718481517"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1002045544935")

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hamzann:hamza00@cluster0.id2lo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "PyFiles")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://graph.org/file/c22ccad28832aed94dbf1-49c96f1f7912938b86.jpg https://graph.org/file/8f6cc424fd39cc1795a9a-b391b8231829437915.jpg https://graph.org/file/751ee02f7a14fe4ce2654-bdd2466f2072f43072.jpg https://graph.org/file/c31acfb82bcb6b84cf0db-be7324cab11728ef6d.jpg https://graph.org/file/f11fd5d2e16ed916d99f7-2edcc1fec1f2bf5fa6.jpg https://graph.org/file/538c75cd683fe80e0af06-14fa7fe9b96606d462.jpg https://graph.org/file/32d4b831e2c75ab5386a7-f197828d183b0223fd.jpg https://graph.org/file/6435da024bab819bb574d-c252e46c3fd92f0245.jpg https://graph.org/file/b2f3dafcceffd24c4c7aa-e88337d53cfe8bb5f8.jpg https://graph.org/file/d4900277f86fae78586d3-e07cbaf8611b928019.jpg https://graph.org/file/19e15ec483ec1b7656b09-fef4ad2d01c0bc4552.jpg https://graph.org/file/babf5708d7b0ea534a17c-0eb69cf7275020b3fe.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

USER_REPLY_TEXT = "<blockquote>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</blockquote>"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
