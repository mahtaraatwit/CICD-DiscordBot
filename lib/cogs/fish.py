import asyncio
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Member
from typing import Optional
from random import choice


from discord.ext import tasks


class Fish(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="fish")
    async def say_fish_back(self, ctx):
        await ctx.send(f"A good fishy day to you, {ctx.author.mention} sir")

    @command(name="fishy")
    async def donda(self, ctx):
        await ctx.send("Fish!")


def setup(bot):
    bot.add_cog(Fish(bot))
