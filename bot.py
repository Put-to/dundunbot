from logging import exception
import discord
import os, random
import requests
import json
import time
from discord.ext import tasks, commands


bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
bot.remove_command('help')

if not os.path.isfile("config.json"): #Replace with config.json
    print("Config file not found")
    exit()
else :
    with open("config.json") as file:
        config = json.load(file)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    status_task.start()
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension '{filename}'")
            except Exception as e:
                exception = f"{type(e).__name__} : {e}"
                print(f"Failed to load extension {filename} \n {exception}")
    



@tasks.loop(minutes = 3.0)
async def status_task():
    statuses = ["Under Testing", "Maintenance", "Still Dumb", "Learning"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("The command you specified was not found.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Enter arguments.")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    with open("blacklist.json") as file:
        blacklist = json.load(file)
    if message.author.id in blacklist["ids"]:
        return
    await bot.process_commands(message)


bot.run(config["token"])
