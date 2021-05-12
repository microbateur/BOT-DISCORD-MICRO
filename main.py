import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix = "!")



print("test")

#fermeture du bot
@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()
    print("Bot Closed")
    

bot.run("ODQyMDkxODI3OTA4OTY4NDc3.YJwRIQ.IOckQmLlgoR9BJq391CVZOYHUbo")