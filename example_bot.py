import discord
import os
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='$')

@bot.command()
async def empty(ctx):
    await ctx.send("empty")

@bot.command()
async def hello(ctx, foo):
    await ctx.send("Hello "+ctx.author)


bot.run(os.environ['BOT_TOKEN'])