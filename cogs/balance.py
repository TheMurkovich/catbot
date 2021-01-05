import discord
from discord.ext import commands

from pymongo import MongoClient


class Balance(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="balance", aliases=["bal"])
    async def balance(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(embed=discord.Embed(title=f"Баланс **{ctx.author}**",
                                               description=f"Баланс: **{self.collection.users.find_one({'id': ctx.author.id})['cash']}**<:infiniticoin:777091801453690910>",
                                               colour=discord.Colour.blue()))
        else:
            await ctx.send(embed=discord.Embed(title=f"Баланс **{member}**",
                                               description=f"Баланс: **{self.collection.users.find_one({'id': member.id})['cash']}**<:infiniticoin:777091801453690910>",
                                               colour=discord.Colour.blue()))


def setup(client):
    client.add_cog(Balance(client))
