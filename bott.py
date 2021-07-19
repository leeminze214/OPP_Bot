from typing import Awaitable
import discord 
from discord.ext import commands
import discord.utils


token = open('tok.txt').read()
bot = bot = commands.Bot(command_prefix='.', help_command =None, case_insensitive=True)
reactionRoleChannelId = 866761663020662784
emojisRoles = {
    "😃":"test",
    "🙈":"Sober"

}

@bot.event
async def on_ready():
    print('opp bot is on!')


@bot.command(aliases = ['rrm'])
async def reactionRoleMessage(ctx):
    channel = bot.get_channel(reactionRoleChannelId) 
    embed = discord.Embed()
    embed.title = ""
    name = "**What types of opportunities are you interested in?**"
    value = """test"""
    embed.add_field(name=name,value=value)
    rrmsg = await channel.send(embed=embed)
    for emoji in emojisRoles:
        await rrmsg.add_reaction(emoji)
      

@bot.event
async def on_reaction_add(reaction,user):
    if reaction.message.channel.id != reactionRoleChannelId:
        return
    if reaction.emoji in emojisRoles.keys():
        roleName = emojisRoles[reaction.emoji]
        role = discord.utils.get(user.guild.roles,name=roleName)
        await user.add_roles(role)
      
# @bot.event
# async def on_reaction_removed(reaction,user):
#     if reaction.message.channel.id != reactionRoleChannelId:
#         return
#     if reaction.emoji in emojisRoles.keys():
#         roleName = emojisRoles[reaction.emoji]
#         role = discord.utils.get(user.guild.roles,name=roleName)      
#         await user.remove_roles(role)






bot.run(token, bot = True)
