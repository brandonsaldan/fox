# ---------------------
# ported to discord by /u/exofeel
# ---------------------
# orginally coded by @4201337
# ---------------------
# ported to python3 by brensalsa

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import urllib.request


bot = commands.Bot(command_prefix='%')



@bot.event
async def on_ready():
    print("Kitsune is ready.")

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kitsune(ctx, network, username):
    if network == "twitter":
        url = 'https://www.twitter.com/'
        print("command recieved.")
        req = requests.get(url + username)
        if req.status_code == 200:
            embed = discord.Embed(title="Twitter Request", color=0x00aced)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Not Available")
            await bot.say(embed=embed)
        elif req.status_code == 404:
            embed = discord.Embed(title="Twitter Request", color=0x00aced)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Available")
            await bot.say(embed=embed)
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    elif network == "instagram":
        url = 'https://www.instagram.com/'
        req = requests.get(url + username)
        if req.status_code == 200:
            embed = discord.Embed(title="Instagram Request", color=0xbc2a8d)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Not Available")
            await bot.say(embed=embed)
        elif req.status_code == 404:
            embed = discord.Embed(title="Instagram Request", color=0xbc2a8d)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Available")
            await bot.say(embed=embed)
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    elif network == "youtube":
        url = 'https://www.youtube.com/'
        req = requests.get(url + username)
        if req.status_code == 200:
            embed = discord.Embed(title="YouTube Request", color=0xff0000)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Not Available")
            await bot.say(embed=embed)
        elif req.status_code == 404:
            embed = discord.Embed(title="YouTube Request", color=0xff0000)
            embed.add_field(name="Username", value="{}".format(username))
            embed.add_field(name="Status", value="Available")
            await bot.say(embed=embed)
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    else:
        await bot.say("Sorry, that social media is currently not supported.")

@kitsune.error
async def kitsune_error(error, ctx):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        userID = (ctx.message.author.id)
        await bot.send_message(ctx.message.channel,"<@%s>: **Please provide a social media and/or a username.**" % (userID))
        await bot.delete_message(ctx.message)

bot.run('insert bot token here')
