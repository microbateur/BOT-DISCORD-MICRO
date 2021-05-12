import discord
from discord.ext import commands
import random
import time
import asyncio

from discord.user import User

#prefix
bot = commands.Bot(command_prefix = "!")

#utilisateur discord
client = discord.Client()


###################################################
#                     DEBUT                       #
###################################################


print("LAUNCH")


###################################################
#                  FERMETURE                      #
###################################################


#fermeture du bot
@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()
    print("Bot Closed")
    

###################################################
#                  AUTO REPONSE                   #
###################################################


@bot.event
async def on_message(message):
# Liste de message et d'émoji
    Ewink = bot.get_emoji(842166658633695243)
    EGulag = bot.get_emoji(799687664060203028)
    EEyes = bot.get_emoji(842167759248556052)
    AutoR = ["Mais NON!","Ah Oui " + str(Ewink) ,"Genre","Okem Cool " + str(EGulag),"Alors peut-être", "Attention " + str(EEyes)]
# User
    user = [492278387038093312,683018314611687549] #Id de la cible
# Auto Message
    if  message.author.id in user :
        
        CHANNEL_ID = message.channel.id
        CHANNEL = bot.get_channel(CHANNEL_ID) #CHANNEL_ID = le message dans le bon channel
        await CHANNEL.send(random.choice(AutoR)) # Message récup de la Liste de message
        #await CHANNEL.send(EGulag)
#    


#################################################
#################################################

bot.run("ODQyMDkxODI3OTA4OTY4NDc3.YJwRIQ.IOckQmLlgoR9BJq391CVZOYHUbo")