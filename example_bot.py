import discord
import os
from discord.ext import commands
import logging
import re

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


# plot from X to Y
plotRegex = re.compile(r'^from (\d*) ?, ?(\d*) ?to ?(\d*) ?, ?(\d*)')


@bot.command()
async def plot(ctx, *, args):
    match = plotRegex.match(args)
    if not match:
        await ctx.send("Invalid plot command.  Ex: 'plot from 25,6 to 32,9'")
    else:
        from_x = match.group(1)
        from_y = match.group(2)
        to_x = match.group(3)
        to_y = match.group(4)

        await ctx.send(f'I should probably do math on going from {from_x},{from_y} over to {to_x},{to_y}')

bot.run(os.environ['BOT_TOKEN'])
