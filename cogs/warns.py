import discord
from discord.ext import commands

from pymongo import MongoClient


class Warns(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "")
        self.db = self.cluster[""]
        self.collection = self.db[""]

    @commands.command(name="warns")
    async def warns(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed(title=f"Количество предов у {ctx.author}",
                                description=f"У Вас **{self.collection.users.find_one({'id': ctx.author.id})['warns']}**",
                                colour=discord.Colour.blue())
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"Количество предов у {member}",
                                description=f"У него **{self.collection.users.find_one({'id': member.id})['warns']}**",
                                colour=discord.Colour.blue())
            await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Warns(client))
