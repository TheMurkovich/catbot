import discord
from discord.ext import commands
from pymongo import MongoClient


class Setbio(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "")
        self.db = self.cluster[""]
        self.collection = self.db[""]

    @commands.command(name="setbio")
    async def setbio(self, ctx, *, arg=None):
        if arg is None:
            await ctx.send(
                embed=discord.Embed(title="Ошибка", description="Укажите аргументы!", colour=discord.Colour.red()))
        else:
            em = self.client.get_emoji(775778315112808449)
            await ctx.message.add_reaction(em)
            self.collection.users.update_one({"id": ctx.author.id}, {"$set": {"bio": arg}})


def setup(client):
    client.add_cog(Setbio(client))
