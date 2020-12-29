import discord
from discord.ext import commands

from pymongo import MongoClient

import random


class MoneyBags(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient("mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name='moneybags', aliases=['mb'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def moneybags(self, ctx):
        bal = self.collection.users.find_one({'id': int(ctx.author.id)})['cash']
        rand = random.randint(1, 100)
        if rand <= 30:
            emb = discord.Embed(title="Мешки", description="Вы открыли мешок, а там ничего не было", colour=discord.Colour.gold())
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title="Мешки", description=f"Вы открыли мешок и там было {rand} <:infiniticoin:777091801453690910>!", colour=discord.Colour.gold())
            self.collection.users.update_one({'id': int(ctx.author.id)}, {'$set': {'cash': int(bal)+int(rand)}})
            await ctx.send(embed=emb)


def setup(client):
    client.add_cog(MoneyBags(client))