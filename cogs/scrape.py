import discord
import asyncio
import requests
import urllib.request
import datetime
import os

from discord.ext import commands
from discord.ext.commands import Bot

social_networks = {"instagram": "https://www.instagram.com/", "twitter": "https://www.twitter.com/", "reddit": "https://www.reddit.com/user/", "soundcloud": "https://soundcloud.com/"}
social_network_prefix = {"instagram": "@", "twitter": "@", "reddit": "/u/", "soundcloud": ""}

bot = commands.Bot(command_prefix='%')

class Scrape(object):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kitsune(self, ctx, network, username):
        try:
            try:
                social_url = social_networks[network]
                req = requests.get(social_url + username, headers = {'User-agent': 'Kitsune Username Scraper'})
                username_prefix = social_network_prefix[network]
                if req.status_code == 200:
                    #await self.bot.say("{}{} is unavailable.".format(username_prefix, username))
                    if network == "twitter":
                        embed = discord.Embed(title="Twitter Request", color=0x20c0eb)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Unavailable")
                        await self.bot.say(embed=embed)
                        print("Twitter request recieved. Input is unavailable.")
                        print("----------------------")
                    elif network == "instagram":
                        embed = discord.Embed(title="Instagram Request", color=0xfe139e)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Unavailable")
                        await self.bot.say(embed=embed)
                        print("Instagram request recieved. Input is unavailable.")
                        print("----------------------")
                    elif network == "reddit":
                        embed = discord.Embed(title="Reddit Request", color=0xf08a0d)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Unavailable")
                        await self.bot.say(embed=embed)
                        print("Reddit request recieved. Input is unavailable.")
                        print("----------------------")
                    elif network == "soundcloud":
                        embed = discord.Embed(title="SoundCloud Request", color=0xff8800)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Available")
                        await self.bot.say(embed=embed)
                        print("SoundCloud request recieved. Input is available.")
                        print("----------------------")
                elif req.status_code == 404:
                    #await self.bot.say("{}{} is Available.".format(username_prefix, username))
                    if network == "twitter":
                        embed = discord.Embed(title="Twitter Request", color=0x20c0eb)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Available")
                        await self.bot.say(embed=embed)
                        print("Twitter request recieved. Input is available.")
                        print("----------------------")
                    elif network == "instagram":
                        embed = discord.Embed(title="Instagram Request", color=0xfe139e)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Available")
                        await self.bot.say(embed=embed)
                        print("Instagram request recieved. Input is available.")
                        print("----------------------")
                    elif network == "reddit":
                        embed = discord.Embed(title="Reddit Request", color=0xf08a0d)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Available")
                        await self.bot.say(embed=embed)
                        print("Reddit request recieved. Input is available.")
                        print("----------------------")
                    elif network == "soundcloud":
                        embed = discord.Embed(title="SoundCloud Request", color=0xff8800)
                        embed.add_field(name="Username", value="{}".format(username_prefix + username))
                        embed.add_field(name="Status", value="Available")
                        await self.bot.say(embed=embed)
                        print("SoundCloud request recieved. Input is available.")
                        print("----------------------")
                else:
                    await self.bot.say("Error! *{}*".format(req.status_code))
                    print("Error.")
                    print("----------------------")
            except Exception as e:
                await self.bot.say(":warning: **Critical error!**  \n{}".format(e))
                print("Critical error.")
                print("----------------------")
        except CommandOnCooldown as p:
            await self.bot.say("{}".format(p))

    @bot.event
    async def on_command_error(self, error, ctx):
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            userID = (ctx.message.author.id)
            await self.bot.send_message(ctx.message.channel,"<@%s>: **Please provide a social media and/or a username.**" % (userID))
            await self.bot.delete_message(ctx.message)
            print("Error - No social media given.")
            print("----------------------")
        elif isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
            userID = (ctx.message.author.id)
            await self.bot.send_message(ctx.message.channel, "{} You're doing that too fast, please slow down.".format(ctx.message.author.mention))
            print("Cooldown message displayed.")
            print("----------------------")

def setup(bot):
    bot.add_cog(Scrape(bot))