import discord
from discord.ext import commands
import traceback

import random

class EightBallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.answers = [
            "It seems likely",
            "No, not at all",
            "Possibly, if you're good",
            "Yes!",
            "No...",
            "Maybe",
            "¯\_(ツ)_/¯",
            "Signs point to yes",
            "Signs point to no",
            "Signs point to possibly",
            "Honestly I don't know",
            "Yes, definitely yes",
            "No, not a chance",
            "Honestly, just believe what you want. I'm just a bot made by some person on the internet. You shouldn't trust me with your question",
            "Hahahahahaha no",
            "Yes yes 1000 times yes!",
            "Maaaaaaaaybeeeeeee",
            "Look, I'm not saying no, but I'm definitely not saying yes",
            "You must believe in the heart of the cards",
            "... Sure, why not",
            "... Sorry, but no",
            "Could you maybe ask again later?",
            "Please try again later",
            "Ask when I'm not so busy doing... Stuff...",
            "Woah look at the time, gotta run!",
            "You know what? Just for you, yes",
            "Nope!"
        ]

    @commands.command(name='eightball', aliases=['8ball', '8b'])
    async def eightball(self, ctx, *, question: str = None):
        if question == None:
            await ctx.send("You'll need to ask a question")
            return
        await ctx.send(random.choice(self.answers))


def setup(bot):
    bot.add_cog(EightBallCog(bot))
