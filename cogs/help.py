import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def help(self, ctx):
        emb = discord.Embed(title="Меню помощи",
                            description='**Термины:**\n`args` - аргументы команды. Например "Привет".\n`num` - число. Например "1".\n`user` - Упоминание участника. Например "<@632923863507927041>".\n**Обозначения:**\n`[]` - Обязательный параметр.\n`<>` - Необязательный параметр.',
                            colour=discord.Colour.green())
        emb.add_field(name="Команды",
                      value="**i.say [args]** - Даёт писать от имени бота. Нужно право управление сообщениями.\n**i.help** - Это сообщение.\n**i.ping** - Пинг бота.\n**i.info** - Информация о боте.\n**i.rand [num1] [num2]** - Выдаёт случайное число от `[num1]` и до `[num2]`.\n"
                            "**i.clear [num]** - Очищает сообщения в канале. Нужно право управление сообщениями.\n**i.avatar <user>** - Показывает аватар участника.\n**i.percent [args]** - Показывает вероятность `[args]`.\n**i.server** - Показывает информацию о сервере.\n"
                            "**i.setbio [args]** - Установит биографию.\n**i.bio <user>** - Покажет биографию.\n**i.buy [args]** - Купит товар с названием `[args]`.\n**i.shop** - Покажет магазин.\n**i.bal <user>** - Покажет баланс `<user>.`\n**i.work** - Работа\n**i.moneybags** - Мешки.\n**i.snow** - Уборка снега.")

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Help(client))
