import asyncio
from http import client
import imp
from multiprocessing.connection import Listener
from tabnanny import check 
from discord.ext.commands import Cog 
from discord.ext import commands
from discord.ext.commands import command
from discord import Member
from discord import channel
from discord import File


class Octopus(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_miggy(ctx):
        print(ctx.author.name)
        return ctx.author.id == 462771945046409227
    
    @commands.check(is_miggy)
    @commands.command(name="octopus")
    async def he_is_here(self, ctx):
        if check:
            print("we checked")
            await ctx.send(file=File('lib\cogs\pus.jpg'))

def setup(bot):
    bot.add_cog(Octopus(bot))

#await channel.history(limit=100, check=check).flatten()