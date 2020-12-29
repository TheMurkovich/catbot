import discord
from discord.ext import commands

import random

class Rand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='rand')
    async def rand(self, ctx, arg1, arg2):
        num1 = int(arg1)
        num2 = int(arg2)
        emb = discord.Embed(title='Рандомное число', description=f'Вам выпало **__{random.randint(num1, num2)}__**!',
                            colour=discord.Colour.blue())
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Rand(client))