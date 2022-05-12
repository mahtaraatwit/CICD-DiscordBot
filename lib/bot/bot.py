# importing asyncio, discord.py and datetime for scheduler


from discord import Embed
from discord.ext.commands.bot import Bot as BotBase
from glob import glob

from discord import Intents
import asyncio
from datetime import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

#from apscheduler.schedulers.asyncio import AsyncIOScheduler
#from apscheduler.triggers.cron import CronTrigger


COGS = ["fish", "octopus"]

EMBEDS = [path.split("\\")[-1][:-3] for path in glob("./lib/embed/*.py")]

PREFIX = "+"
OWNER_ID = [732756725685289023]

TOKEN = os.environ.get('TOKEN')


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.TOKEN = TOKEN

        #self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_ID,
            intent=Intents.all())

    def run(self):

        print("running setup ...")

        self.setup()

        print("running fishy bot...")
        super().run(self.TOKEN, reconnect=True)

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

    async def fish_spam(self):
        await self.channel.send("Fish!")

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(876646255940476929)
            self.channel = self.get_channel(882732917300805662)

            print("bot ready")

        else:
            print("bot reconnected")




