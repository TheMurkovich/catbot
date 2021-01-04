import discord
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='avatar', aliases=['ava'])
    async def avatar(self, ctx, *, member: discord.Member = None):  # set the member object to None
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author

        emb = discord.Embed(title=f'Аватар **{member.name}#{member.discriminator}**',
                            description='[Открыть в браузере]({0})'.format(member.avatar_url),
                            colour=discord.Colour.blue())
        emb.set_image(url=member.avatar_url)

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Avatar(client))