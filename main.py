import discord
import json
import os
import datetime
import aiohttp
import requests
import datetime
from aiohttp import request
import requests
import typing as t
import time
from typing import Optional
from discord.ext import commands
from discord import Member
from config import *
import pyfiglet
import time
import random
from random import choice
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="?", help_command=None)

print("Bot Is Ready")
print("Logged In As Silk")
print("No Errors Found")
print("Working Nicely")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"?help"))

@client.command()
async def help(ctx):
  e = discord.Embed(
  title="Silk Commands!",
  description="howgay, howcute, simprate, pp, whendie, say, ascii, hack, coinflip, randomnumber, ping, invite",
    color=0xFF0000
)
  await ctx.send(embed=e)
 
@client.command()
async def simprate(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(
            title="Calculating how simp you are...",
            color=0xFF0000
        )
        msg = await ctx.message.reply(embed=embed)

        cute_number = random.randint(0, 100)

        if 0 <= cute_number <= 20:
            embed_color = 0xFF0000
        if 20 < cute_number <= 50:
            embed_color = 0xFF0000
        if 50 < cute_number <= 100:
            embed_color = 0xFF0000

        embed = discord.Embed(
            title="Simprate Detecter!",
            description=f"**{user.name}#{user.discriminator}** is **{cute_number}%** simp!",
            color=0xFF0000
        )

        await msg.edit(embed=embed)

@client.command()
async def say(ctx, *, text=''):
    if text == '':
        await ctx.send("You need to say something")
    else:
       await ctx.send(text)

@client.command()
async def hack(ctx, user: discord.Member = None):
        if user == None:
            await ctx.message.reply(embed=discord.Embed(
                title = "Error!",
                description = "You didn't mention who to hack. Please try again!",
                color = 0xFF0000
            ))

        elif user == ctx.author:
            await ctx.message.reply("You shouldn't hack yourself.")

        else:
            email_fun = ['69420', '8008135', 'eatsA$$', 'PeekABoo',
                            'TheShire', 'isFAT', 'Dumb_man', 'Ruthless_gamer',
                            '69', 'Loyalboy69', 'likesButts']

            email_address = f"{user.name.lower()}{random.choice(email_fun).lower()}@gmail.com"
                            
            passwords = ['animeislife69420', 'big_awoogas', 'red_sus_ngl',
                            'IamACompleteIdiot', 'YouWontGuessThisOne',
                            'yetanotherpassword', 'iamnottellingyoumypw',
                            'SayHelloToMyLittleFriend', 'ImUnderYourBed',
                            'TellMyWifeILoveHer', 'P@$$w0rd', 'iLike8008135', 'IKnewYouWouldHackIntoMyAccount',
                            'BestPasswordEver', 'JustARandomPassword']
                            
            password = f"{random.choice(passwords)}"

            DMs = ["send nudes please", "i invited silk and i got  nothing lol",
                    "i hope my mum doesn't find my bad paper result",
                    "please dont bully me", "https://youtu.be/oHg5SJYRHA0", 
                    "i like bananas", "black jellybeans are the best jellybeans",
                    "i use discord in light mode"]

            latest_DM = f"{random.choice(DMs)}"

            ip_address = f"690.4.2.0:{random.randint(1000, 9999)}"

            Discord_Servers = ["Sons of Virgins", "Small Benis Gang", "Gamers United",
                                    "Anime_Server_69420", "CyberDelayed 2077", "I love Corn"]

            Most_Used_Discord_Server = f"{random.choice(Discord_Servers)}"


            msg1 = await ctx.send("Initializing Hack.exe...")
            await asyncio.sleep(1)

            real_msg1 = await ctx.channel.fetch_message(msg1.id)
            await real_msg1.edit(content = f"Successfully initialized Hack.exe, beginning hack on {user.name}... ")
            await asyncio.sleep(1)

            real_msg2 = await ctx.channel.fetch_message(msg1.id)
            await real_msg2.edit(content = f"Logging into {user.name}'s Discord Account...")
            await asyncio.sleep(1)

            real_msg3 = await ctx.channel.fetch_message(msg1.id)
            await real_msg3.edit(content = f"Logged into {user.name}'s Discord:\nEmail Address: `{email_address}`\nPassword: `{password}`")
            await asyncio.sleep(1)

            real_msg4 = await ctx.channel.fetch_message(msg1.id)
            await real_msg4.edit(content = f"Fetching DMs from their friends(if there are any)...")
            await asyncio.sleep(1)

            real_msg5 = await ctx.channel.fetch_message(msg1.id)
            await real_msg5.edit(content = f"Latest DM from {user.name}: `{latest_DM}`")
            await asyncio.sleep(1)

            real_msg6 = await ctx.channel.fetch_message(msg1.id)
            await real_msg6.edit(content = f"Getting IP address...")
            await asyncio.sleep(1)

            real_msg7 = await ctx.channel.fetch_message(msg1.id)
            await real_msg7.edit(content = f"IP address found: `{ip_address}`")
            await asyncio.sleep(1)

            real_msg11 = await ctx.channel.fetch_message(msg1.id)
            await real_msg11.edit(content = f"Fetching the Most Used Discord Server...")
            await asyncio.sleep(1)

            real_msg10 = await ctx.channel.fetch_message(msg1.id)
            await real_msg10.edit(content = f"Most used Discord Server in {user.name}'s Account: `{Most_Used_Discord_Server}`")
            await asyncio.sleep(1)

            real_msg8 = await ctx.channel.fetch_message(msg1.id)
            await real_msg8.edit(content = f"Selling data to the dark web...")
            await asyncio.sleep(1)

            real_msg9 = await ctx.channel.fetch_message(msg1.id)
            await real_msg9.edit(content = f"Hacking complete.")
            await ctx.send(f"{user.name} has successfully been hacked.\n\n**{user.name}**'s Data:\nDiscord Email: `{email_address}`\nDiscord Password: `{password}`\nMost used Discord Server: `{Most_Used_Discord_Server}`\nIP Address: `{ip_address}`\nLatest DM: `{latest_DM}`")
            
@client.command()
async def ascii(ctx, *, text = None):
        if text == None:
            await ctx.message.reply(f"Please enter some text.")
        else:
            if len(pyfiglet.figlet_format(text)) > 2000:
                await ctx.message.reply(f"Text too long. Please enter short text.")
            else:
                await ctx.message.reply(f"```{pyfiglet.figlet_format(text)}```")

@client.command()
async def howgay(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(
            title="Calculating how gay you are...",
            color=0xFF0000
        )
        msg = await ctx.message.reply(embed=embed)

        cute_number = random.randint(0, 100)

        if 0 <= cute_number <= 20:
            embed_color = 0xFF0000
        if 20 < cute_number <= 50:
            embed_color = 0xFF0000
        if 50 < cute_number <= 100:
            embed_color = 0xFF0000

        embed = discord.Embed(
            title="Gayness Detector!",
            description=f"**{user.name}#{user.discriminator}** is **{cute_number}%** gay!",
            color=0xFF0000
        )

        await msg.edit(embed=embed)

@client.command()
async def pp(ctx):
    x = random.randint(1,10)
    e = discord.Embed(
  title="Calculated PP",
  description=f"8{'='*random.randint(1, 10)}D",
    color=0xFF0000
    )
    await ctx.send(embed=e)

determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!", color=0xFF0000)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!", color=0xFF0000)
        await ctx.send(embed=embed)

@client.command()
async def randomnumber(ctx):
    x = random.randint(1,100)
    e = discord.Embed(
  title="Random Number Is",
  description=f"{x}",
    color=0xFF0000
)
    await ctx.send(embed=e)

@client.command()
async def invite(ctx):
  e = discord.Embed(
  title="My Invite Link And My Support Server Link Here!",
  description="My Invite Link [here](https://discord.com/api/oauth2/authorize?client_id=853611248440180746&permissions=2148005952&scope=bot) And My Support Server [here](https://discord.gg/Ry33J6qPZE)",
    color=0xFF0000
  )
  await ctx.send(embed=e)
  
@client.command()
async def howcute(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(
            title = "Calculating cuteness...",
            color = 0xFF0000
        )
        msg1 = await ctx.message.reply(embed=embed)

        cute_number = random.randint(0, 100)

        if 0 <= cute_number <= 20:
            lol = "Damn, you're ugly!"
            embed_color = 0xFF0000
        if 20 < cute_number <= 50:
            lol = "Not bad!"
            embed_color = 0xFF0000
        if 50 < cute_number <= 75:
            lol = "You're kinda cute, UwU"
            embed_color = 0xFF0000
        if 75 < cute_number <= 100:
            lol = "Holy fuck, you're cute! ><"
            embed_color = 0xFF0000

        embed = discord.Embed(
            title="Cuteness detector!",
            description = f"**{user.name}#{user.discriminator}** is **{cute_number}%** cute!",
            embed_color = 0xFF0000
        )
        embed.set_footer(text=lol)

        await msg1.edit(embed=embed)
    
@client.command()
async def whendie(ctx, *, user: discord.Member = None):
        if user == None:
            user = ctx.author

        msg = await ctx.message.reply(embed=discord.Embed(title="Let's see when you're gonna die...", color=0xFF0000))

        something = [
            f'{random.randint(0, 60)} Second(s)',
            f'{random.randint(1, 60)} Minute(s)',
            f'{random.randint(1, 24)} Hour(s)',
            f'{random.randint(1, 7)} Day(s)',
            f'{random.randint(1, 4)} Week(s)',
            f'{random.randint(1, 100)} Year(s)'
        ]

        thingy = random.choice(something)

        if thingy == something[0]:
            funny_text = "LOL YOU'RE DEAD"
            embed_color = 0xFF0000
        if thingy == something[1]:
            funny_text = "Well rip, you're almost dead"
            embed_color = 0xFF0000
        if thingy == something[2]:
            funny_text = "Sad"
            embed_color = 0xFF0000
        if thingy == something[3]:
            funny_text = "Ok you have some time before you die"
            embed_color = 0xFF0000
        if thingy == something[4]:
            funny_text = "not dying that early, Yay!"
            embed_color = 0xFF0000
        if thingy == something[5]:
            funny_text = "Wowie, you have a nice long life! OwO"
            embed_color = 0xFF0000

        embed = discord.Embed(
            description = f"{user.mention} is gonna die in **{thingy}**",
            color = 0xFF0000
        )
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_footer(text=funny_text)

        await msg.edit(embed=embed)

@client.command()
async def ping(ctx):

        time1 = time.time()

        msg = await ctx.message.reply(embed=discord.Embed(title = "Pong", color=0x00FFFF))

        embed = discord.Embed(
            title = "Pong!",
            description = f"""
**{round((time.time() - time1) * 1000)}ms**
            """,
            color = 0xFF0000
        )

        await msg.edit(embed=embed)

client.run(os.getenv('token'))
