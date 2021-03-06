import discord
from discord.ext import commands

# add package to path
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

import discordbotdash.dash as dbd # pylint: disable=no-name-in-module, import-error

# load from env
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["TOKEN"]

bot = commands.AutoShardedBot("b!")

@bot.command()
async def hi(ctx):
    """Says hi"""
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    """Says bye"""
    await ctx.send("Bye!")

@bot.command()
async def morning(ctx):
    """Says morning"""
    await ctx.send("Good morning!")

@bot.command()
async def afternoon(ctx):
    """Says afternoon"""
    await ctx.send("Good afternoon!")

@bot.command()
async def evening(ctx):
    """Says evening"""
    await ctx.send("Good evening!")

@bot.event
async def on_ready():
    initial_extensions = ["cogs.one", "cogs.two"]

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            
        except:
            print(f"{extension} failed to load.")
    
    print(f"Logged in as {bot.user} | {bot.user.id}")
    dbd.openDash(bot)

bot.run(TOKEN)