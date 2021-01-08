import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def help(self, ctx):
        emb = discord.Embed(
            description='**Термины:**\n`args` - аргументы команды. Например "Привет".\n`num` - число. Например "1".\n`user` - Упоминание участника. Например "<@632923863507927041>".\n**Обозначения:**\n`[]` - Обязательный параметр.\n`<>` - Необязательный параметр.',
            colour=discord.Colour.green())
        emb.add_field(name="Команды",
                      value="**i.say [args]** - Даёт писать от имени бота. Нужно право управление сообщениями.\n**i.help** - Это сообщение.\n**i.ping** - Пинг бота.\n**i.info** - Информация о боте.\n**i.rand [num1] [num2]** - Выдаёт случайное число от `[num1]` и до `[num2]`.\n"
                            "**i.clear [num]** - Очищает сообщения в канале. Нужно право управление сообщениями.\n**i.avatar <user>** - Показывает аватар участника.\n**i.percent [args]** - Показывает вероятность `[args]`.\n**i.server** - Показывает информацию о сервере.\n"
                            "**i.setbio [args]** - Установит биографию.\n**i.bio <user>** - Покажет биографию.\n**i.buy [args]** - Купит товар с названием `[args]`.\n**i.shop** - Покажет магазин.\n**i.bal <user>** - Покажет баланс `<user>.`\n**i.work** - Работа\n**i.moneybags** - Мешки.\n**i.snow** - Уборка снега.\n**i.help-2** - Вторая страница.")
        await ctx.send(embed=emb)

    @commands.command(name="help-2")
    async def help2(self, ctx):
        emb = discord.Embed(
            description='**Термины:**\n`args` - аргументы команды. Например "Привет".\n`num` - число. Например "1".\n`user` - Упоминание участника. Например "<@632923863507927041>".\n**Обозначения:**\n`[]` - Обязательный параметр.\n`<>` - Необязательный параметр.',
            colour=discord.Colour.green())
        emb.add_field(name="Команды",
                      value="**i.kick [user]** - Кикнет `member`.\n**i.mute [member] [time] [reason]** - Замутит участника на `time` __секунд__.\n**i.unban [member] [reason] - Разбанит участника.\ni.unmute [member] [reason]** - Размутит участника.\n**i.warn [member] [reason]** - Даст пред участнику.\n**i.unwarn [member] [reason]** - Снимет пред у участника.\n**i.warns <member>** - Покажет список предов.")
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Help(client))
