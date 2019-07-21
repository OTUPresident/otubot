import discord
from discord.ext import commands
import traceback

import os

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = {
        "FBIT": 597999102655070208,
        "FED": 598000133929435136,
        "FESNS": 597999412052230164,
        "FEAS": 597999173463179274,
        "FHS": 597999326505205761,
        "FS": 597999271173685248,
        "FSSH": 598000927244550154,
        }

        self.commands = [
            ['help', 'Display this message'],
            ['f', 'Pay your respects'],
            ['8ball', 'Ask the magic Murphy'],
            ['nsfw', 'Admit your degeneracy and gain access to the NSFW channel'],
            ['github', 'For those who want to contribute to OTUBot'],
            ['custom', 'Make your own commands!']
        ]

    @commands.command(name='help')
    async def help(self, ctx):
        # await ctx.send("https://tenor.com/view/cat-no-ones-around-to-help-dance-gif-12006069")
        msg = "```\n"
        for command, info in self.commands:
            msg += '{:<{width}} {:<} {:<}\n'.format(command, '-' * (10 - len(command)), info, width=len(command))
        msg += '```'
        await ctx.send(msg)

    @commands.command(name="github")
    async def github(self, ctx):
        await ctx.send("https://github.com/OTUPresident/otubot")

    @commands.command(name="nsfw", aliases=['NSFW'])
    async def nsfw(self, ctx):
        await ctx.author.add_roles(ctx.guild.get_role(599360290252914714))
        await ctx.message.delete()

    @commands.command(name='faculty')
    async def faculty(self, ctx, *, fac: str = None):
        if ctx.guild.get_role(598002582408921109) in ctx.author.roles:
            await ctx.send("You've already set your faculty")
            return

        if fac == None:
            await ctx.send("""Please use `!faculty <acronym>` to choose your faculty!
```
FBIT  - Faculty of Business and Information Technology
FED   - Faculty of Education
FESNS - Faculty of Energy Systems and Nuclear Science
FEAS  - Faculty of Engineering and Applied Science
FHS   - Faculty of Health Sciences
FS    - Faculty of Science
FSSH  - Faculty of Social Science and Humanities
OTHER - In case you'd rather not identify with a faculty```IE: !faculty FEAS""")
            return

        if fac.upper() in ["OTHER"]:
            await ctx.author.add_roles(ctx.guild.get_role(598002582408921109))
            return

        if fac.upper() in ["FBIT", "FED", "FESNS", "FEAS", "FHS", "FS", "FSSH", "OTHER"]:
            await ctx.author.add_roles(ctx.guild.get_role(self.roles[fac.upper()]), ctx.guild.get_role(598002582408921109))
            return

        await ctx.send("That is not a valid faculty")

def setup(bot):
    bot.add_cog(GeneralCog(bot))
