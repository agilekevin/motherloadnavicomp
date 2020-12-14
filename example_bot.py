import discord
import os
from discord.ext import commands
import logging

from discord.ext.commands import Bot

logging.basicConfig(level=logging.INFO)

bot: Bot = commands.Bot(command_prefix='$')


@bot.command()
async def empty(ctx):
    await ctx.send("empty")


@bot.command()
async def hello(ctx, foo):
    await ctx.send("Hello "+foo)


@bot.command()
async def hungry(ctx):
    await ctx.send("food")


bot.run(os.environ['BOT_TOKEN'])
