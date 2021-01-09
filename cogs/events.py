import datetime
import colorama
import discord
from colorama import Fore
from discord.ext import commands
from pymongo import MongoClient


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot ready!')
        print('[DATA_BASE] Connected')
        print("Sended!")
        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Game('New Year!'))
        for guild in self.client.guilds:
            for member in guild.members:
                post = {"id": member.id,
                        "name": member.name,
                        "discrim": member.discriminator, "bot": member.bot,
                        "system": member.system, "cash": 0,
                        "bio": "Нету биографии",
                        "dev": False,
                        "new-year2020": False,
                        "warns": 0
                        }
                if self.collection.users.count_documents({"id": member.id}) == 0:
                    self.collection.users.insert(post)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        post = {"id": member.id, "name": member.name, "discrim": member.discriminator, "bot": member.bot,
                "system": member.system, "cash": 0, "bio": "Нету биографии", "dev": False, "new-year2020": False, "warns": 0}
        if self.collection.users.count_documents({"id": member.id}) == 0:
            self.collection.users.insert(post)

    @commands.Cog.listener()
    async def on_message(self, message):
        if '<@&777493284435525662>' in message.content:
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        elif '<@&777493289234333776>' in message.content:
            await message.add_reaction('🎮')
        elif message.channel == self.client.get_channel(777493347245621268):
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        if message.content == "<@746468518144507925>":
            await message.channel.send(f"{message.author.mention}, `i.help`")
        if message.channel == self.client.get_channel(777493354661019698):
            if message.author.id == 746468518144507925:
                pass
            else:
                await message.channel.send("<@&777493287391985725>")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(title="Ошибка",
                                               description=f"Вы достигли кулдауна этой команды, попробуйте через **{round(error.retry_after)}** секунд",
                                               colour=discord.Colour.red()))
            pass
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(
                embed=discord.Embed(title="Ошибка", description=f"Участник не найден!", colour=discord.Colour.red()))
            pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"Отсутствуют аргументы команды!",
                                               colour=discord.Colour.red()))
            pass
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(title="Ошибка", description=f"Аргументы введены некорректно!",
                                               colour=discord.Colour.red()))
            pass
        else:
            colorama.init()
            await ctx.send(embed=discord.Embed(title="Ошибка",
                                               description=f"Произошла ошибка и я не смог выполнить эту команду. Обратитесь к <@632923863507927041>.",
                                               colour=discord.Colour.red()))
            print(Fore.RED + "[ERR!] " + Fore.WHITE + f"Error date - {datetime.datetime.now()}. Error:\n{error}")


def setup(client):
    client.add_cog(Events(client))
