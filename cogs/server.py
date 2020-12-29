import discord
from discord.ext import commands

class Server(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="server")
    async def server(self, ctx):
        regions = {
            'europe' : ":flag_eu: Европа",
            'russia' : ":flag_ru: Россия",
            'brazil' : ":flag_br: Бразилия",
            'hongkong' : ":flag_hk: Гонконг",
            'india' : ":flag_in: Индия",
            'japan' : ":flag_jp: Япония",
            'singapore' : ":flag_sg: Сингапур",
            'southafrica' : ":flag_sa: Южная Африка",
            'sydney' : ":flag_au: Сидней",
            'us-central' : ":flag_us: Центральная США",
            'us-east' : ":flag_us: Восточная США",
            'us-south' : ":flag_us: Южная США",
            'us-west' : ":flag_us: Западная США"
        }
        region = regions[str(ctx.guild.region)]
        embed = discord.Embed(title="Информация о сервере", description=f"Название сервера: **{str(ctx.guild.name)}**\nРегион сервера: **{region}**", colour=discord.Colour.blue())
        embed.add_field(name="Каналы", value=f"<:channels:775048970253893654> Всего каналов: **{len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}**\n<:textchannel:775048275287998504> Текстовые каналы: **{len(ctx.guild.text_channels)}**\n<:voicechannel:775048661419425853> Голосовые каналы: **{len(ctx.guild.voice_channels)}**", inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Участники", value=f":person_frowning: Всего участников: **{ctx.guild.member_count}**", inline=False)
        embed.add_field(name="Владелец сервера", value=f"<:owner:745996885382266880> {ctx.guild.owner.mention}", inline=False)
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Server(client))