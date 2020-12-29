import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # команда ping
    @commands.command(name="ping", aliases = ['Ping', 'PING', 'pING', 'Пинг', 'ПИНГ', 'пИНГ', 'пинг', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
    async def __ping(self, ctx): # Объявление асинхронной функции __ping с возможностью публикации сообщения
        ping = round(self.client.latency * 1000) # Получаем пинг клиента

        if ping < 130:
            ping_emoji = "<:online:758637420798935041>"
            ping_color = discord.Colour.green()

        if ping > 130:
            ping_emoji = "<:idle:758637503514148884>"
            ping_color = discord.Colour.gold()

        if ping > 200:
            ping_emoji = "<:dnd:758637536691879948>"
            ping_color = discord.Colour.red()

        if ping > 300:
            ping_emoji = "<:offline:758637450070982656>"
            ping_color = discord.Colour(696969)


        EmbedPing = discord.Embed(title="Пинг", description=f"**{ping_emoji} Пинг бота:** {ping}", colour=ping_color)
        await ctx.send(embed=EmbedPing) # Редактирование первого сообщения на итоговое (на сам пинг)


def setup(client):
    client.add_cog(Ping(client))