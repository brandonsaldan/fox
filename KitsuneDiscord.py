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

social_networks = {"instagram": "https://www.instagram.com/", "twitter": "https://www.twitter.com/", "youtube": "https://www.youtube.com/", "reddit": "https://www.reddit.com/user/"}
social_network_prefix = {"instagram": "@", "twitter": "@", "youtube": " ", "reddit": "/u/"}


@bot.event
async def on_ready():
    print("Kitsune is ready.")

@bot.command(pass_context=True)
async def kitsune(ctx, network, username):
    try:
        social_url = social_networks[network]
        req = requests.get(social_url + username, headers = {'User-agent': 'Kitsune username checker'})
        username_prefix = social_network_prefix[network]
        if req.status_code == 200:
            await bot.say("{}{} is unavailable.".format(username_prefix, username))
        elif req.status_code == 404:
            await bot.say("{}{} is Available.".format(username_prefix, username))
        else:
            await bot.say("Error! *{}*".format(req.status_code))
    except Exception as e:
        await bot.say(":warning: **Critial error!**  \n{}".format(e))

@kitsune.error
async def kitsune_error(error, ctx):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        userID = (ctx.message.author.id)
        await bot.send_message(ctx.message.channel,"<@%s>: **Please provide a social media and/or a username.**" % (userID))
        await bot.delete_message(ctx.message)

bot.run('insert bot token here')
