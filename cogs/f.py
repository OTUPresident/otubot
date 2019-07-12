import discord
from discord.ext import commands
import traceback

class FCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='f')
    async def f(self, ctx, *, user: discord.Member = None):
        if user == None:
            await ctx.send("You must @ somebody to pay your respects")
            return
        embed = discord.Embed(color=0x777777)
        embed.description = "**{}** has paid their respects to <@{}>".format(ctx.author.display_name, user.id)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FCog(bot))
