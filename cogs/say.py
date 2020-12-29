import discord
from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='say')
    async def say(self, ctx, *, arg=None):
        if ctx.author.guild_permissions.manage_messages is True:
            if arg is None:
                await ctx.send(f"{ctx.author.mention}, что мне сказать?")
            else:
                await ctx.send(arg)
                print(f'{ctx.author.id} sended: {arg}')
        else:
            await ctx.send(f"{ctx.author.mention}, у Вас нет прав!")


def setup(client):
    client.add_cog(Say(client))

