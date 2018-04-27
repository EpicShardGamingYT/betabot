import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

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
        
    if message.content.startswith('=bye'):
        msg = 'GoodBye {0.author.mention} Hope To See You Again Soon :wave: '.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('=test'):
        if message.author.id == "344967220025098242":
            msg = 'Hello {0.author.mention} How Are You Today'.format(message)
            await client.send_message(message.channel, msg)
        else: 
            await client.send_message(message.channel, "Only Jackaboi#8319 can use this command")
   

client.run(os.getenv('TOKEN'))
