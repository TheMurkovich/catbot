import discord
from discord.ext import commands

from pymongo import MongoClient
from asyncio import sleep


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="mute")
    async def mute(self, ctx, member: discord.Member, time, *, reason):
        if ctx.author.guild_permissions.kick_members is True:
            role = discord.utils.get(ctx.guild.roles, id=783350807964680242)
            await member.add_roles(role)
            await ctx.message.add_reaction("✅")
            await member.send(
                f"Вас замутили на сервере **{ctx.guild.name}**! До размута: {time} секунд. Причина: {reason}")
            await sleep(int(time))
            await member.remove_roles(role)
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Mute(client))
