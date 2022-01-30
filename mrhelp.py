import discord
import os
from dotenv import load_dotenv
import random

bot = discord.Bot()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

testing_servers = [684237072827154435, 920013664604553246]
prefix = "$"

# Welcome message for when the bot comes online      
@bot.event
async def on_ready():
    print(f"{bot.user} Has logged on")
    for server in bot.guilds:
        print(server)
  
# Filters out messages that don't start with the $ sign
@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        elif message.content[0] != "$":
            return
    except:
        return "Their was an error handling the message"
    
    # Initializes the user who sent the message along with grabbing message content
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    #help command
    if user_message.lower() == f"{prefix}help":
        response = """
```
$help Displays all commands
$random Gives you a random number
$hello Gives you a hello
$echo Echo
```
"""
        await message.channel.send(response)
        return
    # random command
    elif user_message.lower() == f"{prefix}random":
        response = f"This is your random number, {random.randint(1, 1000)}"
        await message.channel.send(response)
        return
    # hello command
    elif user_message.lower() == f"{prefix}hello": 
        await message.channel.send(f"Hello, {username}")
        return
    # echo command
    elif user_message.startswith(f"{prefix}echo"):
        echoc = user_message.replace("$echo", "")
        await message.channel.send(f"**echo**{echoc}")
        return


# slash commands
@bot.slash_command(guild_ids=testing_servers, name="hello", description="Says hello")
async def hello(ctx):
    await ctx.respond("Hello!")
    return
 
@bot.slash_command(guild_ids=testing_servers, name="random", description="Generates a random number")
async def random_num(ctx):
    response = f"This is your random number, {random.randint(1, 1000)}"
    await ctx.respond(response)

@bot.slash_command(guild_ids=testing_servers, name="help", description="Displays all $ commands")
async def help(ctx):
    response = """
```
$help Displays all commands
$random Gives you a random number
$hello Gives you a hello
$echo Echo
```
"""
    await ctx.respond(response)
    
bot.run(TOKEN)