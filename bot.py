import os

import discord
from discord.ext import commands
from pymongo import MongoClient

from config import settings

cluster = MongoClient(
    "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
db = cluster["Cherrydb"]
collection = db["CherryCollection"]
intents = discord.Intents(messages=True, guild_messages=True, members=True, guilds=True)
client = commands.Bot(command_prefix=collection.find_one("settings")["prefix"], intents=intents)
client.remove_command('help')


@client.command(name="load", aliases=["l"])
async def load(ctx, extension):
    if ctx.author.id == collection.find_one("settings")["owner_id"]:
        try:
            client.load_extension(f"cogs.{extension}")
            await ctx.message.add_reaction("😎")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            await ctx.send(f"```py\n{e}```")
    else:
        await ctx.message.add_reaction("⛔")


@client.command(name="unload", aliases=["unl"])
async def unload(ctx, extension):
    if ctx.author.id == collection.find_one("settings")["owner_id"]:
        try:
            client.unload_extension(f"cogs.{extension}")
            await ctx.message.add_reaction("😎")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            await ctx.send(f"```py\n{e}```")
    else:
        await ctx.message.add_reaction("⛔")


@client.command(name="reload", aliases=["r"])
async def reload(ctx, extension):
    if ctx.author.id == collection.find_one("settings")["owner_id"]:
        try:
            client.unload_extension(f"cogs.{extension}")
            client.load_extension(f"cogs.{extension}")
            await ctx.message.add_reaction("😎")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            await ctx.send(f"```py\n{e}```")
    else:
        await ctx.message.add_reaction("⛔")


for filename in os.listdir("/bot/CherryBotPython/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        

client.run(settings['TOKEN'])
