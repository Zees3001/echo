import discord
from discord.ext import commands

class Chantools:
    
	""" Channel Infos """

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
	async def onlineusers(chan : str):
	    """Adds two numbers together."""
	    await bot.say(users)