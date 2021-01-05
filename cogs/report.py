import discord
from discord.ext import commands

from pymongo import MongoClient


class Report(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="report")
    async def report(self, ctx, mem: discord.Member = None, reason=None):
        if mem and reason is not None:
            em = discord.Embed(title="Новый репорт!",
                               description=f"Новый репорт на пользователя **{mem}**! Причина: **{reason}**",
                               colour=discord.Colour.blue())
            em.set_thumbnail(url=mem.avatar_url)
            em.set_footer(text=f"Отправлен {ctx.author}", icon_url=ctx.author.avatar_url)
            await self.client.get_channel(777493363564871691).send("@here", embed=em)
            await ctx.send(
                f"{ctx.author.mention}, Ваша жалоба успешно отправлена и вскоре будет рассмотрена модераторами!")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description="Отсутствуют аргументы команды!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Report(client))
