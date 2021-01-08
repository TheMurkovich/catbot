import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="ban")
    async def ban(self, ctx, member: discord.Member, *, reason):
        if ctx.author.guild_permissions.ban_members is True:
            await member.send(f"Вы были забанены на сервере **{ctx.guild.name}**! Причина: {reason}")
            await member.ban(reason=reason, delete_message_days=0)
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Ban(client))
