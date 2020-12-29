import discord
from discord.ext import commands

import ast

from pymongo import MongoClient

from asyncio import sleep

import json

import requests

import subprocess


class DevCmds(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(
            "mongodb+srv://TheMurkovich:EMvQ6bqhcAoCOD9S@cherrybot.9k23u.mongodb.net/Cherrydb?retryWrites=true&w=majority")
        self.db = self.cluster["Cherrydb"]
        self.collection = self.db["CherryCollection"]

    def insert_returns(self, body):
        # insert return stmt if the last expression is a expression statement
        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])
        # for if statements, we insert returns into the body and the orelse
        if isinstance(body[-1], ast.If):
            self.insert_returns(body[-1].body)
            self.insert_returns(body[-1].orelse)
        # for with blocks, again we insert returns into the body
        if isinstance(body[-1], ast.With):
            self.insert_returns(body[-1].body)

    @commands.command(name='eval', aliases=['e'])
    async def eval_fn(self, ctx, *, cmd=None):
        if self.collection.users.find_one({"id": ctx.author.id})["dev"] is True:
            if cmd is None:
                await ctx.send(f"{ctx.author.mention}, bruh")
                return
            try:
                fn_name = "_eval_expr"
                cmd = cmd.strip("` ")

                # add a layer of indentation
                cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

                # wrap in async def body
                body = f"async def {fn_name}():\n{cmd}"

                parsed = ast.parse(body)
                body = parsed.body[0].body

                self.insert_returns(body)

                env = {
                    'client': ctx.bot,
                    'discord': discord,
                    'commands': commands,
                    'ctx': ctx,
                    '__import__': __import__,
                    'mongo': self.collection,
                    'requests': requests,
                    'json': json,
                    'sleep': sleep
                }
                exec(compile(parsed, filename="<ast>", mode="exec"), env)

                result = (await eval(f"{fn_name}()", env))

                if result is None:
                    await ctx.send(f"{ctx.author.mention}, bruh")
                    return

                await ctx.send(f"```py\nCompleted\n{result}```")
            except Exception as e:
                await ctx.send(f"```py\nError\n{e}```")
        else:
            await ctx.send(f'{ctx.author.mention}, ты кто что-бы использовать евал? Вот именно никто.')

    @commands.command(name='off')
    async def off(self, ctx):
        if self.collection.users.find_one({"id": ctx.author.id})["dev"] is True:
            em = self.client.get_emoji(775778315112808449)
            await ctx.message.add_reaction(em)
            await self.client.close()
        else:
            await ctx.send(f'{ctx.author.mention}, ты кто что-бы перезапускать бота? Вот именно никто.')

    @commands.command(name='activity')
    async def activ(self, ctx, *, arg):
        if self.collection.users.find_one({"id": ctx.author.id})["dev"] is True:
            await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(arg))
            em = self.client.get_emoji(775778315112808449)
            await ctx.message.add_reaction(em)
        else:
            await ctx.send(f"{ctx.author.mention}, no")

    @commands.command(name="nickname", aliases=["nick"])
    async def change_nickname(self, ctx, *, name: str = None):
        if self.collection.users.find_one({"id": ctx.author.id})["dev"] is True:
            try:
                await ctx.guild.me.edit(nick=name)
                if name:
                    await ctx.send(f"Ник установлен на **{name}**!")
                else:
                    await ctx.send("Ник удалён!")
            except Exception as err:
                await ctx.send(err)
        else:
            await ctx.send(f"{ctx.author.mention}, no")

    @commands.command(name="exec")
    async def exec(self, ctx, *, cmd):
        if self.collection.users.find_one({"id": ctx.author.id})["dev"] is True:
            try:
                a = subprocess.check_output(cmd, shell=True)
                await ctx.send(f"```py\nCompleted\n{a}```")
            except Exception as e:
                await ctx.send(f"```py\nError\n{e}```")
        else:
            await ctx.send(f"{ctx.author.mention}, no")


def setup(client):
    client.add_cog(DevCmds(client))
