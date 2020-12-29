import discord
from discord.ext import commands


class Message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="prv")
    async def mes(self, ctx):
        emb = discord.Embed(title="Правила сервера INFINITI",
                            description="**1. Основные положения**\n1.1 Все участники сервера равны перед правилами.\n1.2 Мат разрешен, но не злоупотреблять им. (Мут на 15 минут)\n1.3 Запрещены оскорбления. (Мут на 1 час)\n1.4 Запрещен NSFW-контент (порнография, шок-контент). (Бан навсегда, исключение nsfw каналы)\n1.5 Запрещен жесткий троллинг. (Бан на 2 часа)\n1.6 Запрещен любой вид флуда. (Мут на 35 минут)\n1.7 Запрещено злоупотребление капсом. (Варн при игнорировании мут на 30 минут)\n1.8 Соблюдайте [Условия использования Discord](https://discord.com/terms) и [Правила сообществ Discord](https://discord.com/guidelines)\n1.9 Запрещается оффтопить (сообщения не по теме). (Мут на 30 минут или предупреждение зависит от тяжести нарушения)\n\n**2.Положения размещения ссылок**\n2.1 Запрещена реклама без согласования с управлением сервера. (Бан навсегда)\n2.2 Запрещена спам-рассылка в личные сообщения других участников. (Бан навсегда)\n2.3 Запрещено оставлять ссылки на вредоносные файлы/приложения. (Бан на 5 дней)\n\n**3. Положения голосового чата**\n3.1 Запрещено включать в свой микрофон музыку. (Мут в голосовом канале на 20 минут)\n3.2 Запрещено издавать громкие звуки в микрофон (т.е. дуть в микрофон, подносить его близко ко рту и т.д.). (Мут в голосовом канале на 25 минут)\n3.3 Если у вас на фоне много шума, используйте функцию Push-To-Talk. (Кик из голосового канала)\n\n**4. Ник**\n4.1 Запрещены оскорбительные никнеймы. (Варн при игнорировании кик)\n4.2 Запрещены залго никнеймы. (Просьба сменить ник при игнорировании кик)\n4.3 Запрещено копировать никнеймы. (Просьба сменить ник при игнорировании кик)\n\n**5. Статус**\n5.1 Запрещены оскорбительные статусы. (Просьба сменить статус при игнорировании кик)\n\n**6. Упоминания**\n6.1 Запрещено упоминать @everyone/@here без причины. (Мут на 35 минут)\n6.2 Запрещено слишком много упоминать роли и участников они тоже люди. (Мут на 25 минут)",
                            colour=discord.Colour.blue())
        emb.add_field(name="Наказания за предупреждения",
                      value="4 преда - мут на 20 минут.\n7 предов - мут на 1 час.\n10 предов - кик.\n15 предов - бан на 2 дня.\n20 предов - бан навсегда.")
        await ctx.send(embed=emb)
        emb2 = discord.Embed(
            description="Я молодец, так как:\n1. Я прочёл правила выше и согласен с ними;\n2. Выполнил все пункты выше и хочу получить доступ к остальным каналам, нажав на реакцию :white_check_mark: ниже.",
            colour=discord.Colour.blue())
        emb2.set_image(
            url="https://cdn.discordapp.com/attachments/758374417092575232/787680792917966878/download_3.gif")
        await ctx.send(embed=emb2)

    @commands.command(name="rol")
    async def rol(self, ctx):
        emb = discord.Embed(title="Список ролей", colour=discord.Colour.blue())
        emb.add_field(name="Специальные роли",
                      value="<@&777493243629011005> - Владелец сервера\n<@&777493244820193290> - Администратор сервера\n<@&777493247094292500> - Помощник администратора\n<@&777493248808845322> - Главный модератор\n<@&777493249610219540> - Модератор\n<@&777493250072117249> - Смотрящие сервера\n<@&777493251111780362>  - Участники котороые проходят стажировку\n<@&777493252668260362> - Должностные лица сервера, которые ушли в отставку\n<@&777493271735173122> - Участник сервера\n<@&777493251585605633> - Ютуберы\n<@&740906482874187888> - Бустер сервера\n<@&777493266866110476> - Партнёр сервера\n<@&777493267923206154> - За голос и комент на [сайте](https://server-discord.com/716940718890942507)\n<@&777493269521235968> - Тот кто был на величайшем событии\n<@&777493271395041280> - За актив и адекватность\n<@&777493253380767764> - За помощь серверу")
        emb.add_field(name="Уровни/ранги",
                      value="<@&777493280296009728> - 5 Уровень\n<@&777493279520063488> - 10 Уровень\n<@&777493278475419681> - 15 Уровень\n<@&777493277736828998> - 20 Уровень\n<@&777493276516155422> - 25 Уровень\n<@&777493275564965909> - 30 Уровень\n<@&777493274528186379> - 35 Уровень\n<@&777493273912147978> - 40 Уровень")
        emb.add_field(name="Покупные роли",
                      value="<@&780060641939030026> - 1000 <:infiniticoin:777091801453690910>\n <@&780061894471188520> - 3500 <:infiniticoin:777091801453690910>\n <@&780062953881862156> - 5500 <:infiniticoin:777091801453690910>\n <@&777493259689525259> - 10000 <:infiniticoin:777091801453690910> ")
        emb.set_image(url="https://cdn.discordapp.com/attachments/758374417092575232/787687810127757342/download.gif")

        await ctx.send(embed=emb)

    @commands.command(name="rr")
    async def rr(self, ctx):
        em = discord.Embed(title="Основные роли",
                           description="🥥 - <@&777493284435525662>\n⬆ - <@&777493286251659267>\n⚠ - <@&777493287391985725>\n🎇 - <@&777493288336228383>\n🔻 - <@&777493289234333776>\n🧒 - <@&777493291440406559>\n🧑 - <@&777493292626608128>",
                           colour=discord.Colour.blue())
        em.set_image(url="https://cdn.discordapp.com/attachments/758374417092575232/787690177740144660/download_2.gif")
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Message(client))
