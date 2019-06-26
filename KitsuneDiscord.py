# orginally coded by 4201337
# ported to discord by exofeel
# created by exofeel, brensalsa, clemente, and padraig

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import urllib.request
import datetime
import os

from os import listdir
from os.path import isfile, join

from discord.ext import commands
import logging
import traceback

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("Kitsune is ready.")
    print("----------------------")
    number_of_servers = len(bot.servers)
    await bot.change_presence(game=discord.Game(name='Prefix: %'.format(number_of_servers)))

@bot.command(pass_context=True)
async def kitsune_help(ctx):
    print("Help command recieved.")
    print("----------------------")
    embed = discord.Embed(title="Kitsune is a simple social media username scraping Discord bot.", colour=discord.Colour(0xffb25d), description="Please fully read all commands.", timestamp=datetime.datetime.utcfromtimestamp(1526316493))

#embed.set_image()
#embed.set_thumbnail()
    embed.set_author(name="Kitsune Help Command")
    embed.set_footer(text="Kitsune")

    embed.add_field(name="Default prefix", value="The default prefix is currently %. We will add support for changing the prefix in chat, however you can change the prefix in the source code.")
    embed.add_field(name="%kitsune", value="Usage: \n```%kitsune [platform] [username]``` \nThe current supported social networks are: \n\n-Reddit\n-Instagram\n-Twitter\n-SoundCloud\n")
    embed.add_field(name="%batch", value="Kitsune can do batches of usernames inside a .txt file. Please seperate each username into it's own line. Any other format can break the bot and make the social network think weirdly about future requests.\n\nUsage:\n```%batch [network] [url to .txt file]```")
    embed.add_field(name="Have a suggestion?", value="**u/exofeel**\n\n**bren#8026**\n\n**/u/lafterr**\n\n**Padraig#1020**", inline=True)
    embed.add_field(name="Donations?", value="\n \n**Vertcoin**:*VhYdqgeBmudv3wuDwNB4VhuQzNjK3Rw9n7* \n**Ethereum**:*0x6CC93E2E2D4dd0430Bab5d8Bb71a395090B84026*", inline=True)

    await bot.say(embed=embed)

number_of_servers = len(bot.servers)
social_networks = {"instagram": "https://www.instagram.com/", "twitter": "https://www.twitter.com/", "reddit": "https://www.reddit.com/user/", "soundcloud": "https://soundcloud.com/"}
social_network_prefix = {"instagram": "@", "twitter": "@", "reddit": "/u/", "soundcloud": ""}

@bot.command(pass_context=True)
async def batch(ctx, network, url, force="false"):
    r = requests.get(url)
    #usernames = []
    f = open('temp.txt', 'w+')
    f.write(r.text)
    with open('temp.txt','r') as f:
        usernames = [line.strip() for line in f]
        print(usernames)
        username_count = len(usernames)
        if force == "true":
            if username_count >= 999:
                await bot.say("I'm sorry, but 75 usernames is the limit. Please remove some before continuing.")
                print("Batch error - Too many usernames given.")
                print("----------------------")
            else:
                pass   
        else:
            await bot.say("Usernames detected: {}".format(username_count))
            try:
                    available_names = []
                    unavailable_names = []
                    error_names = []
                    available_names_number = len(available_names)
                    unavailable_names_number = len(available_names)
                    scraped_usernames = available_names_number + unavailable_names_number
                    embed = discord.Embed(title="Kitsune Username Scraper.", colour=discord.Colour(0xfe139e), description="Loading!", timestamp=datetime.datetime.utcfromtimestamp(1526305073))

                    embed.set_thumbnail(url="http://www.slashfilm.com/wp/wp-content/images/Zootopia-Nick-Wilde.jpg")
                    embed.set_footer(text="Kitsune Username Scraper")

                    embed.add_field(name="Available names ✅", value="{}".format(available_names))
                    embed.add_field(name="Unavailable names :no_entry:", value="{}".format(unavailable_names))
                    embed.add_field(name="Names that returned an error :warning:", value="{}".format(error_names))

                    message = await bot.say(embed=embed)
                    message
                    for x in usernames:
                        print("Checking username {}".format(x))
                        social_url = social_networks[network]
                        req = requests.get(social_url + x, headers = {'User-agent': 'Kitsune Username Scraper'})
                        username_prefix = social_network_prefix[network]
                        if req.status_code == 200:
                            unavailable_names.append(x)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                        elif req.status_code == 404:
                            #await bot.say("{}{} is Available.".format(username_prefix, username))
                            available_names.append(x)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                        else:
                            #x.append(error_names)
                            error_names.append(x)
                            names_list = str(available_names)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                            #await bot.say(available_names)
                        embed = discord.Embed(title="Instagram Username Scraper", colour=discord.Colour(0xfe139e), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                        if network == "instagram":
                            embed = discord.Embed(title="Instagram Username Scraper", colour=discord.Colour(0xfe139e), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="https://instagram-brand.com/wp-content/uploads/2016/11/app-icon2.png")
                            print("Instagram batch request recieved.")
                            print("----------------------")
                            pass
                        elif network == "twitter":
                            embed = discord.Embed(title="Twitter Username Scraper", colour=discord.Colour(0x20c0eb), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="http://logos-download.com/wp-content/uploads/2016/02/Twitter_logo_bird_transparent_png-700x568.png")
                            print("Twitter batch request recieved.")
                            print("----------------------")
                            pass
                        elif network == "reddit":
                            embed = discord.Embed(title="Reddit Username Scraper", colour=discord.Colour(0xf08a0d), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="https://is5-ssl.mzstatic.com/image/thumb/Purple125/v4/36/b8/a9/36b8a9e3-55ff-d52c-ea7e-974414f925f0/source/100x100bb.jpg")
                            print("Reddit batch request recieved.")
                            print("----------------------")
                        elif network == "soundcloud":
                            embed = discord.Embed(title="SoundCloud Username Scraper", colour=discord.Colour(0xff8800), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="http://icons.iconarchive.com/icons/danleech/simple/1024/soundcloud-icon.png")
                            print("SoundCloud batch request recieved.")
                            print("----------------------")        
                        else:
                            await bot.say("Error")
                            print("Error.")
                            print("----------------------") 
                        embed.set_footer(text="Kitsune Username Scraper")

                        embed.add_field(name="Available names ✅", value="{}".format(available_names))
                        embed.add_field(name="Unavailable names :no_entry:", value="{}".format(unavailable_names))
                        embed.add_field(name="Names that returned an error :warning:", value="{}".format(error_names))
                        await bot.edit_message(message, embed=embed)
                    await bot.say("Done scraping ✅")
            except Exception as e:
                await bot.say(":warning: Critical Error! {}".format(e))
                print("Critical error.")
                print("----------------------")

@bot.command(pass_context=True)
async def reload_all(ctx):
        if ctx.message.author.id == "261953350860275713":
            # Loading
            for extension in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
                try:
                    if not "__init__" in extension:
                        print("Reloading {}...".format(extension))
                        bot.unload_extension("cogs." + extension)
                        loadingCogMessage = await bot.say("Loading {}..".format(extension))
                        bot.load_extension("cogs." + extension)
                        await bot.edit_message(loadingCogMessage, "✅ | {} has been loaded.".format(extension))
                except Exception as e:
                    print("Failed to load cog {}".format(extension))
                    await bot.say("⛔️ | Failed to load cog {}".format(extension))
                    traceback.print_exc()
        else:
            print("Unauthorized user has attempted to reload modules.. Stopped :)")
            await bot.say("⛔️ | Bot owner only!")

async def LoadCogs():
    for extension in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            if not "__init__" in extension:
                print("Loading {}...".format(extension))
                bot.load_extension("cogs." + extension)
        except Exception as e:
            print("Failed to load cog {}".format(extension))
            traceback.print_exc()


def Main():
    logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    Main()

bot.run('')
