import discord
from discord.ext import commands

from pymongo import MongoClient


class UnWarn(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="unwarn")
    async def unwarn(self, ctx, member: discord.Member, *, reason):
        warns = self.collection.users.find_one({"id": member.id})
        if ctx.author.guild_permissions.kick_members is True:
            if warns["warns"] == 0:
                await ctx.send(f"У него нет варнов! 👺👺👺👺")
            else:
                self.collection.users.update_one({"id": member.id}, {"$set": {"warns": warns["warns"] - 1}})
                await member.send(f"С Вас было снято предупреждение на сервере **{ctx.guild.name}**! Причина: {reason}")
                await ctx.message.add_reaction("✅")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(UnWarn(client))
