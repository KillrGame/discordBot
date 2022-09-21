from email import message
from collections import Counter
import random
from discord.ext import commands
from discord import Permissions
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

#intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 282247767902912523  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1,6))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul", reference=message)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "test":
        await message.channel.send("pk faire des tests tu es le meilleur", reference=message)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@bot.command()
async def count(ctx):
    online = 0
    offline = 0
    idle = 0
    dnd = 0
    for i in ctx.guild.members:
        if i.status == discord.Status.online:
            online = online + 1
        if i.status == discord.Status.offline:
            offline = offline + 1
        if i.status == discord.Status.idle:
            idle = idle + 1
        if i.status == discord.Status.dnd:
            dnd = dnd + 1
    res = str(online) + " members are online, "+ str(idle) +" are idle and "+ str(offline) +" are off the do not disturb are " + str(dnd)
    await ctx.send(res)


#token = "MTAyMjE5MjYzOTE3NDUyOTA1NQ.G5uvFJ.OUZg81DKOEs-RmsgqzgcsJidj6j-S-R_7bkeAU"
bot.run(token)  # Starts the bot