# +++ Made By [telegram username: @Here_remo] +++

from aiohttp import web
from plugins.web_server import web_server

import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT, OWNER_ID


# ===== ASCII BANNER =====
BANNER = r"""
$$\                                $$\ $$\                                     $$\                       $$\                               
$$ |                               $$ |\__|                                    $$ |                      $$ |                              
$$ |      $$$$$$\   $$$$$$\   $$$$$$$ |$$\ $$$$$$$\   $$$$$$\         $$$$$$$\ $$ |$$\   $$\  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\        
$$ |     $$  __$$\  \____$$\ $$  __$$ |$$ |$$  __$$\ $$  __$$\       $$  _____|$$ |$$ |  $$ |$$  _____|\_$$  _|  $$  __$$\ $$  __$$\       
$$ |     $$ /  $$ | $$$$$$$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |      $$ /      $$ |$$ |  $$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ |  \__|      
$$ |     $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |      $$ |      $$ |$$ |  $$ | \____$$\   $$ |$$\ $$   ____|$$ |            
$$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$$\ $$ |\$$$$$$  |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |            
\________|\______/  \_______| \_______|\__|\__|  \__| \____$$ |       \_______|\__| \______/ \_______/    \____/  \_______|\__|            
                                                     $$\   $$ |                                                                            
                                                     \$$$$$$  |                                                                            
                                                      \______/                                                                             
"""
# =======================


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        # ===== SHOW BANNER ON VPS =====
        print(BANNER)
        self.LOGGER(__name__).info(BANNER)
        # ==============================

        await super().start()
        bot_info = await self.get_me()
        self.name = bot_info.first_name
        self.username = bot_info.username
        self.uptime = datetime.now()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)

            if not db_channel.invite_link:
                db_channel.invite_link = await self.export_chat_invite_link(CHANNEL_ID)

            self.db_channel = db_channel

            test = await self.send_message(chat_id=db_channel.id, text="Testing")
            await test.delete()

        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make Sure bot is Admin in DB Channel and have proper Permissions, "
                f"So Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info('Bot Stopped..')
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"Fɪʟᴇ-Sʜᴀʀɪɴɢ ʙᴏᴛ Mᴀᴅᴇ Bʏ Tʜᴇ Tᴇᴀᴍ ➪ Lᴏᴀᴅɪɴɢ Cʟᴜꜱᴛᴇʀ"
        )
        self.LOGGER(__name__).info(f"{self.name} Bot Running..!")
        self.LOGGER(__name__).info("OPERATION SUCCESSFULL ✅")

        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

        try:
            await self.send_message(
                OWNER_ID,
                text="<b><blockquote>🤖 Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ ♻️</blockquote></b>"
            )
        except:
            pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info(f"{self.name} Bot stopped.")
