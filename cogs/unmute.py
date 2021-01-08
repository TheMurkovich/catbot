import discord
from discord.ext import commands

from pymongo import MongoClient


class UnMute(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="unmute")
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, id=783350807964680242)
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("Он не замучен! 👺👺👺👺👺👺")


def setup(client):
    client.add_cog(UnMute(client))
