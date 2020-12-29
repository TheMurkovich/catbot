import discord
from discord.ext import commands

from pymongo import MongoClient


class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="shop")
    async def shop(self, ctx):
        if ctx.guild.id == 716940718890942507:
            emb = discord.Embed(title="Магазин", colour=discord.Colour.blue())
            emb.add_field(name="VIP - 1000 <:infiniticoin:777091801453690910> ",
                          value="Ранг **VIP**. Позволяет изменять никнейм и выделятся в списке участников. Имеется так же приоритетный режим для комфортного общения в голосовых каналах.")
            emb.add_field(name="MVP - 3500 <:infiniticoin:777091801453690910> ",
                          value="Ранг **MVP**. Позволяет изменять никнейм,  выделятся в списке участников, доступ к модераторскому каналу. Так же имеется приоритетный режим для комфортного общения в голосовых каналах.")
            emb.add_field(name="MVP+ - 5500 <:infiniticoin:777091801453690910> ",
                          value="Ранг **MVP+**. Позволяет просматривать журнал аудита, изменять никнейм, перемещать участников, доступ к модераторскому каналу и выделятся в списке участников. Дает так же приоритетный режим для комфортного общения в голосовых каналах.")
            emb.add_field(name="Ultimate - 10000 <:infiniticoin:777091801453690910> ",
                          value="Самая высокая и дорогая привилегия на сервере. Те люди, которые смогут приобрести ее, будут считаться легендами экономики.")
            await ctx.send(embed=emb)
        else:
            await ctx.send(f"Эта команда не доступна на данном сервере!")


def setup(client):
    client.add_cog(Shop(client))
