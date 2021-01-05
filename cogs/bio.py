import discord
from discord.ext import commands

from pymongo import MongoClient


class Bio(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="bio")
    async def bio(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed(title=f"Биография {ctx.author}",
                                description=self.collection.users.find_one({"id": ctx.author.id})["bio"],
                                colour=discord.Colour.blue())
            emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"Биография {member}",
                                description=self.collection.users.find_one({"id": member.id})["bio"],
                                colour=discord.Colour.blue())
            emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Bio(client))
