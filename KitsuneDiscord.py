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
async def kitsune(ctx, network, username):
    if network == "twitter":
        url = 'https://www.twitter.com/'
        print("command recieved.")
        req = requests.get(url + username)
        if req.status_code == 200:
            await bot.say("@{} is unavailable.".format(username))
        elif req.status_code == 404:
            await bot.say("@{} is Available.".format(username))
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    elif network == "instagram":
        url = 'https://www.instagram.com/'
        req = requests.get(url + username)
        if req.status_code == 200:
            await bot.say("@{} is unavailable.".format(username))
        elif req.status_code == 404:
            await bot.say("@{} is Available.".format(username))
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    else:
        await bot.say("Sorry that social network is not supported.")

bot.run('insert bot token here')
