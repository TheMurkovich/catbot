import discord
from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="kick")
    async def kick(self, ctx, member: discord.Member = None, *, reason):
        if ctx.author.guild_permissions.kick_members is True:
            await member.send(f"Вас выгнали с сервера **{ctx.guild.name}**! Причина: {reason}")
            await member.kick(reason=reason)
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Kick(client))
