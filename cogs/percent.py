import discord
from discord.ext import commands

import random

class Percent(commands.Cog):

    def __init__(self, client):
        self.client = client

        
    @commands.command(name='percent', aliases=['per'])
    async def percent(self, ctx, arg):
        if arg is None:
            await ctx.send('Где слова?')
        else:
            emb = discord.Embed(title='Вероятность', description=f'Вероятность этого {random.randint(0, 100)}%!',
                                colour=discord.Colour.blue())
            emb.set_footer(text='Эта команда является фановой, не воспринимайте её всерьёз!', icon_url='https://cdn.discordapp.com/attachments/752644617706537070/781863987766755359/emote.png')
            await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Percent(client))