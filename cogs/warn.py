import discord
from discord.ext import commands

from pymongo import MongoClient


class Warn(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "")
        self.db = self.cluster[""]
        self.collection = self.db[""]

    @commands.command(name="warn")
    async def warn(self, ctx, member: discord.Member, *, reason):
        warns = self.collection.users.find_one({"id": member.id})
        if ctx.author.guild_permissions.kick_members is True:
            self.collection.users.update_one({"id": member.id}, {"$set": {"warns": warns["warns"] + 1}})
            await member.send(f"Вам было выдано предупреждение на сервере **{ctx.guild.name}**! Причина: {reason}")
            await ctx.author.send(f"У того кому Вы выдали варн {self.collection.users.find_one({'id': member.id})['warns']} предов. Чекни не надо ли ему выдать бан/мут/кик в правилах")
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Warn(client))
