import discord
import json
import os
from datetime import datetime
import datetime
import aiohttp
import requests
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import datetime
from aiohttp import request
import requests
import typing as t
import time
from keep_alive import keep_alive
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

client.load_extension ('jishaku')

@client.event
async def on_ready():
  print("Bot Is Running!")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"v1.0 | @Silk"))


@client.command()
@commands.guild_only()
async def help(ctx):
  e = discord.Embed(
  title="My All Commands Are Listed Below!!",
  description="\n\n**Fun**\nhowgay, howcute, simprate, pp, whendie, say, 8ball, ascii, hack, randomnumber.\n\n**Games**\ncoinflip, dice, rps/rockpaperscissors\n\n**Sfw**\nslap, hug, pat\n\n**Economy**\nThis Will Be Available Soon!\n\n**Info**\ncovid, source, invite, avatar, ping, bot",
      color=0xFF0000
)
  await ctx.send(embed=e)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def pat(ctx, user: discord.Member = None):
        if user == None:
            await ctx.message.reply(f"Why are you so lonely? Mention someone that you wanna pat, you can't pat yourself :(")
            return

        if user == ctx.author:
            await ctx.message.reply("Imagine patting yourself... why are you so lonely")
            return

        if user == client.user:
            await ctx.message.reply(f"Thank you for patting me><")
            return

        embed = discord.Embed(
			title = "Pat Go Brr",
			description = f"{ctx.author.mention} just patted {user.mention}",
			color = 0xFF0000
			)
        embed.set_image(url=requests.get("https://nekos.life/api/pat").json()['url'])

        await ctx.send(embed=embed)

@client.command()
async def hug(ctx, user: discord.Member = None):
        if user == None:
            await ctx.message.reply(f"Why are you so lonely? Mention someone that you wanna hug, you can't hug yourself :(")
            return

        if user == ctx.author:
            await ctx.message.reply("Imagine hugging yourself... why are you so lonely")
            return

        if user == client.user:
            await ctx.message.reply(f"You hugged me and thanks for the hug! <3")
            return

        embed = discord.Embed(
			title = "hugs OP",
			description = f"this is so cute >< {ctx.author.mention} just hugged {user.mention}",
			color = 0xFF0000
			)
        embed.set_image(url=requests.get("https://nekos.life/api/hug").json()['url'])

        await ctx.send(embed=embed)


@client.command()
async def slap(ctx, user: discord.Member = None):
        if user == None:
            await ctx.message.reply(f"Who do you want to slap idiot? Mention it next time.")
            return

        if user == ctx.author:
            await ctx.message.reply("Imagine slapping yourself... why are you so lonely")
            return

        if user == client.user:
            await ctx.message.reply(f"You slapped me And that slap hurts!")
            return

        embed = discord.Embed(
			title = "Damn boi!",
			description = f"{user.mention} just got slapped by {ctx.author.mention}.",
			color = 0xFF0000
		)
        embed.set_image(url = requests.get("https://nekos.life/api/v2/img/slap").json()['url'])

        await ctx.send(embed=embed)

@client.command(name='rps', aliases=['rockpaperscissors'])
async def rps(ctx):
        """Play Rock, Paper, Scissors game"""
        def check_win(p, b):
            if p=='🌑':
                return False if b=='📄' else True
            if p=='📄':
                return False if b=='✂' else True
            # p=='✂'
            return False if b=='🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != client.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await client.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**Your Choice:\t{reaction.emoji}\nMy Choice:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win**")
            else:
                await ctx.send("**I win :robot:**")


@client.command()
async def dice(ctx):
        embed = discord.Embed(
            title = "Rolling Dice...",
            color = 0xFF0000
        )
        msg = await ctx.message.reply(embed=embed)

        embed = discord.Embed(
            title = "You Rolled It!",
            description=f"You rolled a dice and got **{random.randint(1, 6)}**",
            color = 0xFF0000
        )

        await msg.edit(embed=embed)
        
@client.command(aliases = ['covid-19', 'covid19'])
async def covid(ctx, *, countryName = None):
        try:
            if countryName is None:
                await ctx.send(f"You didn't enter a country name, use the command like this - `?covid [country]`")
            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName.lower()}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title = f"**COVID - 19 Status of {country}**", description = f"This information isn't always live, so it may not be accurate.", color =  0xFF0000)
                embed2.add_field(name = f"Total Cases", value = f"{totalCases}", inline = True)
                embed2.add_field(name = f"Today Cases", value = f"{todayCases}", inline = True)
                embed2.add_field(name = f"Total Deaths", value = f"{totalDeaths}", inline = True)
                embed2.add_field(name = f"Today Deaths", value = f"{todayDeaths}", inline = True)
                embed2.add_field(name = f"Recovered", value = f"{recovered}", inline = True)
                embed2.add_field(name = f"Active", value = f"{active}", inline = True)
                embed2.add_field(name = f"Critical", value = f"{critical}", inline = True)
                embed2.add_field(name = f"Cases Per One Million", value = f"{casesPerOneMillion}", inline = True)
                embed2.add_field(name = f"Deaths Per One Million", value = f"{deathsPerOneMillion}", inline = True)
                embed2.add_field(name = f"Total Tests", value = f"{totalTests}", inline = True)
                embed2.add_field(name = f"Tests Per One Million", value = f"{testsPerOneMillion}", inline = True)
                embed2.set_thumbnail(url = "https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed = embed2)
        except:
            await ctx.send("Invalid Country Lmao")
        
@client.command()
async def bot(ctx):
  embed=discord.Embed(
 title="About Me!",
 description=f"**Hello I Am A Bot Silk, I Am Maded By Dumb Ayush I Was Maded On 15 July 2021 And My Prefix Is - ?, I Am Not That Much Good But I Am Average**",
     color=0xFF0000,
)
  embed.set_footer(text="Thanks!")

  await ctx.send(embed=embed)
 
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() in [f'<@{client.user.id}>', f'<@!{client.user.id}>']:
        return await message.reply(embed = discord.Embed(title=f"You Mentioned Me?", description=f"My Prefix Is - `?`", color=0xFF0000))

    await client.process_commands(message)
  
@client.command(aliases = ['profile', 'pfp'])
async def avatar(ctx, target: Optional[Member]):
        target = target or ctx.author

        embed = discord.Embed(title = f"**Avatar of {target.name}#{target.discriminator}**", color = 0xFF0000)
        embed.set_image(url = target.avatar_url)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed = embed)

@client.command()
@commands.guild_only()
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
@commands.guild_only()
async def say(ctx, *, text=''):
    if text == '':
        await ctx.send("You need to say something")
    else:
       await ctx.send(text)

@client.command()
async def source(ctx):
     e = discord.Embed(
    title="My Source Code!",
    description="My Source Code [Here](https://github.com/lazer6969/-Silk-Bot)",
     color=0xFF0000
)
     await ctx.send(embed=e)

@client.command()
@commands.guild_only()
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

            DMs = ["U Are Mad", "i invited silk and i got  nothing lol",
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
@commands.guild_only()
async def ascii(ctx, *, text = None):
        if text == None:
            await ctx.message.reply(f"Please enter some text.")
        else:
            if len(pyfiglet.figlet_format(text)) > 2000:
                await ctx.message.reply(f"Text too long. Please enter short text.")
            else:
                await ctx.message.reply(f"```{pyfiglet.figlet_format(text)}```")

@client.command()
@commands.guild_only()
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
@commands.guild_only()
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
@commands.guild_only()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!", color=0xFF0000)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!", color=0xFF0000)
        await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def randomnumber(ctx):
    x = random.randint(1,100)
    e = discord.Embed(
  title="Random Number Is",
  description=f"{x}",
    color=0xFF0000
)
    await ctx.send(embed=e)

@client.command()
@commands.guild_only()
async def invite(ctx):
  e = discord.Embed(
  title="My Invite Link And My Support Server Link Here!",
  description="My Invite Link [here](https://discord.com/api/oauth2/authorize?client_id=853611248440180746&permissions=2148005952&scope=bot) And My Support Server [here](https://discord.gg/sA8sttu6Yy)",
    color=0xFF0000
  )
  await ctx.send(embed=e)
  
@client.command()
@commands.guild_only()
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
@commands.guild_only()
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
@commands.guild_only()
async def ping(ctx):

        time1 = time.time()

        msg = await ctx.message.reply(embed=discord.Embed(title = "Pong", color=0xFF0000))

        embed = discord.Embed(
            title = "Pong!",
            description = f"""
**{round((time.time() - time1) * 1000)}ms**
            """,
            color = 0xFF0000
        )

        await msg.edit(embed=embed)

keep_alive()

client.run(os.getenv('token'))
