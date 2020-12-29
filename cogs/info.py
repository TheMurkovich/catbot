import discord
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="info")
    async def info(self, ctx):
        emb = discord.Embed(title="Информация о боте", description="Привет! Я - **CatBot** - самый кошачий бот в Discord.\nМой префикс - `i.`\nЧтобы увидеть список всех моих команд, введите `i.help`", colour=discord.Colour.blue())
        emb.add_field(name="О боте", value="**Язык:** Python\n**Библиотека:** discord.py\n**База данных:** MongoDB\n**Хостинг:** Zomro")
        emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/748174963646660608/775758739159646233/6356e8e3e7ba210b.png")
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Info(client))