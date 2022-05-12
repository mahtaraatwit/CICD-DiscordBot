import asyncio
from http import client
import imp
from multiprocessing.connection import Listener
from tabnanny import check 
from discord.ext.commands import Cog 
from discord.ext.commands import command
from discord import Member
from discord import channel
from discord import File


class Octopus(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def check(ctx):
        return ctx.author.id == 974436550123335721

    @command(name="octupus")
    async def he_is_here(self, ctx):
        if check:
            await ctx.send(file=File('pus.png'))

def setup(bot):
    bot.add_cog(Octopus(bot))

#await channel.history(limit=100, check=check).flatten()