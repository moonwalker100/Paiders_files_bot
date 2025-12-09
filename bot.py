class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
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
            self.LOGGER(__name__).warning(f"Check DB channel permissions, Current CHANNEL_ID: {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot Stopped..")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Aᴅᴠᴀɴᴄᴇ Fɪʟᴇ-Sʜᴀʀɪɴɢ ʙᴏᴛ V3 | Made By @Here_remo")
        self.LOGGER(__name__).info(f"{self.name} Bot Running properly")
        self.LOGGER(__name__).info("OPERATION SUCCESSFULL COMPLETED ✅")

        # Web server setup inside start()
        app_instance = await web_server()                # call the async function
        runner = web.AppRunner(app_instance)             # create AppRunner
        await runner.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(runner, bind_address, PORT).start()

        # Send restart message
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
