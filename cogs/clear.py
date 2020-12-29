import discord
from discord.ext import commands
from asyncio import sleep

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name = "clear")
    async def clear(self, ctx, number=None):
        try:
            if number is None:
                await ctx.send(f"{ctx.author.mention}, введите аргументы!")
            else:
                if ctx.author.guild_permissions.manage_messages is True:
                    number = int(number)
                    if number == 0:
                        await ctx.send(f"{ctx.author.mention}, введите число от 1 до 99!")
                    if number > 99:
                        await ctx.send(f"{ctx.author.mention}, введите число от 1 до 99!")
                    else:
                        await ctx.channel.purge(limit=number+1)
                        await sleep(2.5)
                        embed = discord.Embed(title="Очистка сообщений", description=f"Было удалено {number} сообщений", colour=discord.Colour.blue())
                        await ctx.send(embed=embed)
                else:
                    await ctx.send(f"{ctx.author.mention}, у Вас нет прав!")

        except ValueError:
            await ctx.send(f"{ctx.author.mention}, введите число!")


def setup(client):
    client.add_cog(Clear(client))