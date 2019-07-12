import discord
from discord.ext import commands
import traceback

import os

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension("cogs.{}".format(cog))
            self.bot.load_extension("cogs.{}".format(cog))
        except Exception as e:
            await ctx.send('**`ERROR:\n{}`**'.format(e))
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension("cogs.{}".format(cog))
        except Exception as e:
            await ctx.send('**`ERROR:\n{}`**'.format(e))
        else:
            await ctx.send('**`SUCCESS`**')



def setup(bot):
    bot.add_cog(OwnerCog(bot))
