import discord
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@bot.command
async def hello(ctx):
    await ctx.send("Hello "+ctx.author)

client.run(os.environ['BOT_TOKEN'])