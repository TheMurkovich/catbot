import discord
from discord.ext import commands

import random


class ball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="8ball")
    async def ball(self, ctx, *, args=None):
        responses = ('Да :white_check_mark:',
                     'Нет :x:',
                     'Возможно',
                     'Никак нет :name_badge:',
                     'Кнш',
                     'Да (нет)',
                     'Нет (нет)',
                     'Да (да)',
                     'Нет (да)', 'kek')
        embedError = discord.Embed(title="Ошибка", description="Не были введены аргемуенты",
                                   colour=discord.Colour.red())
        embedLenError = discord.Embed(title="Ошибка", description="Введите текст меньше 1024 символов",
                                      colour=discord.Colour.red())
        if args is None:
            await ctx.send(embed=embedError)
            return
        if args is not None:
            if len(args) >= 1024:
                await ctx.send(embed=embedLenError)
                return
        await ctx.send(random.choice(responses))


def setup(client):
    client.add_cog(ball(client))
