import discord
from discord.ext import commands
import traceback

import sqlite3
from functions import Connection

class CustomCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='custom')
    async def custom(self, ctx, command: str = None, *, output: str = None):
        if command == None:
            await ctx.send("You need to supply a command name")
            return
        if output == None:
            await ctx.send("You need to supply some sort of output")
            return
        conn = Connection('OTUDatabase')
        try:
            conn.queryWithValues("INSERT INTO customCommands VALUES (?,?,?)", (ctx.author.id, command, output))
            await ctx.send("Command added!")
        except:
            await ctx.send("Looks like that command already exists :(")


def setup(bot):
    bot.add_cog(CustomCog(bot))
