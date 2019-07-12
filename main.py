import discord
from discord.ext import commands
import asyncio

import datetime

#Sets the prefix
def get_prefix(bot, message):
    prefixes = ['!']
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Bot description
description = "OTUBot - For managing the OTU Discord"

# Bot cogs
cogs = [
    "cogs.owner",
    "cogs.general"
]

# Global check
def global_check(ctx):
    return ctx.message.author.bot == False

# Create the bot
bot = commands.Bot(
    command_prefix=get_prefix,
    owner_id=427686878616092674,
    description=description,
    # activity=discord.Game("! for help")
)

# Start the show
if __name__ == '__main__':
    bot.add_check(global_check)
    bot.remove_command('help')
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print("Failed to load cog: {}".format(e))

# When everything is ready
@bot.event
async def on_ready():
    print("The bot is ready")
    guild = bot.get_guild(597997811631521792)
    welcomeChannel = guild.get_channel(597997811631521796)
    student = guild.get_role(598002582408921109)
    for member in welcomeChannel.members:
        if member.guild_permissions.administrator == False:
            await member.add_roles(student)

# When user joins
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(597997811631521796)
    await asyncio.sleep(2)
    await channel.send("Welcome to the OTU Discord {}!\nFind and join your faculty by typing `!faculty`".format(member.display_name))

# Minute clock
async def minuteClock():
    await bot.wait_until_ready()
    guild = bot.get_guild(597997811631521792)
    welcomeChannel = guild.get_channel(597997811631521796)
    currentTime = datetime.datetime.now()
    student = guild.get_role(598002582408921109)
    count = 0
    while not bot.is_closed():
        if datetime.datetime.now().hour != currentTime.hour:
            currentTime = datetime.datetime.now()
            count += 1
            if count == 2:
                await welcomeChannel.send("Members will be automatically given the Student role in one hour. If you'd like to select your faculty you have one hour to do so. Use `!faculty` to select your faculty.")
        else:
            await asyncio.sleep(60)
        if count == 3:
            for member in welcomeChannel.members:
                if member.guild_permissions.administrator == False:
                    await member.add_roles(student)
            count = 0

bot.loop.create_task(minuteClock())

# Run the bot
bot.run('', bot=True, reconnect=True)
