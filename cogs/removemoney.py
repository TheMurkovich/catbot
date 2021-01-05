import discord
from discord.ext import commands

from pymongo import MongoClient


class Remove(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="removemoney")
    async def removemoney(self, ctx, arg1: discord.Member, arg2):
        if ctx.author.id == self.collection.find_one("settings")["owner_id"]:
            bal = self.collection.users.find_one({"id": int(arg1.id)})["cash"]
            self.collection.users.update_one({"id": int(arg1.id)}, {'$set': {"cash": bal - int(arg2)}})
            await ctx.send(embed=discord.Embed(title="Добавление денег",
                                               description=f"**Успешно забрано __{arg2}__ <:infiniticoin:777091801453690910> у пользователя __{arg1}__**",
                                               colour=discord.Colour.green()))
        else:
            await ctx.send(f"{ctx.author.mention}, no")


def setup(client):
    client.add_cog(Remove(client))
