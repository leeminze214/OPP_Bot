import discord 
from discord.ext import commands

token = open('tok.txt').read()
bot = bot = commands.Bot(command_prefix='.', help_command =None, case_insensitive=True)

@bot.event
async def on_ready():
    print('opp bot is on!')

print(token)