import discord
from discord.ext import commands

from pymongo import MongoClient

import random


class Work(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="work")
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
        bal = self.collection.users.find_one({"id": ctx.author.id})["cash"]
        rand = random.randint(0, 100)
        self.collection.users.update_one({"id": ctx.author.id}, {"$set": {"cash": bal + rand}})
        await ctx.send(embed=discord.Embed(title="Работа",
                                           description=f"{ctx.author.mention}, вы хорошо поработали и заработали **{rand}**<:infiniticoin:777091801453690910>!",
                                           colour=discord.Colour.gold()))


def setup(client):
    client.add_cog(Work(client))
