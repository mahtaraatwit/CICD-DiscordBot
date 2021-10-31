from discord import Embed as Embeds
from datetime import datetime as dt


class ready_Embed(Embeds):
    def __init__(self, bot):
        self.bot = bot
        self.author = "amen"
        self.footer = timestamp = dt.utcnow()
