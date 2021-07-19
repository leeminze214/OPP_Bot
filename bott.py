import discord 
from discord.ext import commands

token = open('tok.txt').read()
bot = bot = commands.Bot(command_prefix='.', help_command =None, case_insensitive=True)

@bot.event
async def on_ready():
    print('opp bot is on!')

@bot.command
async def reactionRoleMessage(ctx):
    channel = bot.get_channel(866761663020662784) 
    msg = "hi there!"
    await ctx.channel.send(msg)


bot.run(token, bot = True)
