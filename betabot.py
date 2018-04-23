import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "+")
client.remove_command("help")
@client.event
async def on_ready():
    print("Thankyou For Using BETA Bot!")
    await client.change_presence(game=discord.Game(name="BETA"))

@client.event
async def on_message(message):
    if message.content.startswith('+hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)
        
        
        
        
    await client.process_commands(message)
   
    if message.content.startswith('+say'):
        args = message.content.split(" ")
        #args[0] = +say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        
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
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Jackaboi Bot Is Now Online!")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member, time: int, *,reason: str):
    em = discord.Embed(title="User muted!", description=None, color=0x20f911)
    em.add_field(name="User:",value=f"{member}")
    em.add_field(name="Time: ", value=f"{time} min")
    em.add_field(name="Reason: ", value=f"{reason}")
    em.set_thumbnail(url=member.avatar_url)
    role = discord.utils.get(member.server.roles, name="Muted")
    time_min = time * 60
    if ctx.message.author.server_permissions.administrator:
        await client.add_roles(member, role)
        await client.say(" {} Has been muted for {} minutes! :white_check_mark:".format(member.mention, time))
        await asyncio.sleep(time_min)
        await client.remove_roles(member, role)
        await client.say("{} has been unmuted! :smiley:".format(member))     
    else:
        await client.say("You don't have permission to execute this command! :stuck_out_tongue: ")

@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name="Muted")
    if ctx.message.author.server_permissions.administrator:
        await client.remove_roles(member, role)
        await client.say("{} has been unmuted! :white_check_mark: ".format(member.mention))
    else:
        await client.say("You don't have permissions to execute these command! :stuck_out_tongue: ")
   

#Always all if message.content all of then on async def on_message not on bottom
client.loop.create_task(list_servers())
client.run(os.getenv('TOKEN'))
