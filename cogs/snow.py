import discord
from discord.ext import commands

from pymongo import MongoClient

import random

class Snow(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient("mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]
    
    @commands.command(name="snow")
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def snow(self, ctx):
        b = self.collection.users.find_one({"id": ctx.author.id})["cash"]
        r = random.randint(1, 50)
        self.collection.users.update_one({"id": ctx.author.id}, {"$set": {"cash": b + r}})
        await ctx.send(embed=discord.Embed(title="Уборка снега", description=f"{ctx.author.mention}, Вы убрали снег возле гаража и заработали на этом {r}<:infiniticoin:777091801453690910>!", colour=discord.Colour.gold()))


def setup(client):
    client.add_cog(Snow(client))