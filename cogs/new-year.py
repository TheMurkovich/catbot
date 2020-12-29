import discord
from discord.ext import commands
from pymongo import MongoClient


class Ny(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    @commands.command(name="new-year", aliases=["ny"])
    async def ny(self, ctx):
        u = ctx.author
        r = discord.utils.get(u.guild.roles, id=783398239629737994)
        c = self.collection.users.find_one({"id": u.id})["cash"]
        if ctx.guild.id == 716940718890942507:
            if self.collection.users.find_one({"id": u.id})["new-year2020"] is False:
                self.collection.users.update_one({"id": u.id}, {"$set": {"cash": c + 100, "new-year2020": True}})
                await u.add_roles(r)
                await ctx.send(embed=discord.Embed(title="Новый год!",
                                                   description="С Новым годом! Тебе была добавлена роль и 100<:infiniticoin:777091801453690910>!",
                                                   colour=discord.Colour.blue()))
            else:
                await ctx.send(embed=discord.Embed(title="Ошибка", description="Вы уже получили подарок!",
                                                   colour=discord.Colour.red()))
        else:
            pass


def setup(client):
    client.add_cog(Ny(client))