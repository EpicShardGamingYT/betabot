import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "=")
@client.event
async def on_ready():
    print("Thankyou For Using Jackaboi Beta Bot!")
    await client.change_presence(game=discord.Game(name="BETA"))

@client.event
async def on_message(message):
    if message.content.startswith('=hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.author.id == "344967220025098242":
    if message.content.lower().startswith('=test'):
        msg = 'Hello {message.author.mention} How Are You Today'
        await client.send_message(message.channel, msg)
else:
    only Jackaboi#8319 Can Use This Command
client.run(os.getenv('TOKEN'))
