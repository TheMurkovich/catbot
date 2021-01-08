import discord
from discord.ext import commands


class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="unban")
    async def unban(self, ctx, *, member):
        if ctx.author.guild_permissions.ban_members is True:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.message.add_reaction("✅")
        else:
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"{ctx.author.mention}, У Вас нет прав!",
                                               colour=discord.Colour.red()))


def setup(client):
    client.add_cog(Unban(client))
