import discord
from discord.ext import commands

from pymongo import MongoClient


class Buy(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "")
        self.db = self.cluster[""]
        self.collection = self.db[""]

    @commands.command(name="buy")
    async def buy(self, ctx, arg=None):
        if ctx.guild.id == 716940718890942507:
            member = ctx.author
            vip = discord.utils.get(member.guild.roles, id=780060641939030026)
            mvp = discord.utils.get(member.guild.roles, id=780061894471188520)
            mvp2 = discord.utils.get(member.guild.roles, id=780062953881862156)
            ultra = discord.utils.get(member.guild.roles, id=777493259689525259)
            bal = self.collection.users.find_one({"id": member.id})["cash"]
            if arg is None:
                await ctx.send(f"{ctx.author.mention}, Введите товар который Вы хотите купить!")
            else:
                if arg == "VIP":
                    if self.collection.users.find_one({"id": member.id})["cash"] < 1000:
                        await ctx.send(f"{member.mention}, У вас недостаточно средств для покупки ранга **VIP**!")
                    else:
                        await member.add_roles(vip)
                        await ctx.send(f"{ctx.author.mention}, Вы успешно купили ранг **VIP**!")
                        self.collection.users.update_one({"id": member.id}, {"$set": {"cash": bal - 1000}})
                elif arg == "MVP":
                    if self.collection.users.find_one({"id": member.id})["cash"] < 3500:
                        await ctx.send(f"{member.mention}, У вас недостаточно средств для покупки ранга **MVP**!")
                    else:
                        await member.add_roles(mvp)
                        await ctx.send(f"{ctx.author.mention}, Вы успешно купили ранг **MVP**!")
                        self.collection.users.update_one({"id": member.id}, {"$set": {"cash": bal - 3500}})
                elif arg == "MVP+":
                    if self.collection.users.find_one({"id": member.id})["cash"] < 5500:
                        await ctx.send(f"{member.mention}, У вас недостаточно средств для покупки ранга **MVP+**!")
                    else:
                        await member.add_roles(mvp2)
                        await ctx.send(f"{ctx.author.mention}, Вы успешно купили ранг **MVP+**!")
                        self.collection.users.update_one({"id": member.id}, {"$set": {"cash": bal - 5500}})
                elif arg == "Ultimate":
                    if self.collection.users.find_one({"id": member.id})["cash"] < 10000:
                        await ctx.send(f"{member.mention}, У вас недостаточно средств для покупки ранга **Ultimate**!")
                    else:
                        await member.add_roles(ultra)
                        await ctx.send(f"{ctx.author.mention}, Вы успешно купили ранг **Ultimate**!")
                        self.collection.users.update_one({"id": member.id}, {"$set": {"cash": bal - 10000}})
        else:
            await ctx.send(f"Эта команда не доступна на данном сервере!")


def setup(client):
    client.add_cog(Buy(client))
