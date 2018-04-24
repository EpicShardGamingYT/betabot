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
    if message.content.startswith('=bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('=test'):
        msg = 'Goodbye \n{0.author.mention}\n Hope To See You Soon'.format(message)
        await client.send_message(message.channel, msg)    
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
client.run(os.getenv('TOKEN'))
