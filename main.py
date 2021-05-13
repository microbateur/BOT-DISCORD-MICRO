import discord
from discord.ext import commands
import random
import time
from discord.ext.commands.core import command
import youtube_dl
import asyncio
import ffmpeg
import emoji

from discord.user import User

#prefix
bot = commands.Bot(command_prefix = "!")

# Launch Youtube
musics = {}
ytdl = youtube_dl.YoutubeDL()

###################################################
#                     DEBUT                       #
###################################################


print("LAUNCH")


###################################################
#                  AUTO REPONSE                   #
###################################################


@bot.event
async def on_message(message):
# Liste de message et d'émoji
    Ewink = emoji.emojize(":wink:")
    EGulag = bot.get_emoji(799687664060203028)
    EFNews = bot.get_emoji(802274654005755935)
    AutoR = ["Mais NON!","Ah Oui " + str(Ewink) ,"Genre","Okem Cool " + str(EGulag),"Alors peut-être", "Attention " + str(EFNews)]
    print("Listed")
    MSG = message.content
# User
    user = [492278387038093312,683018314611687549,200232047623536640] #Id de la cible
# Auto Message
    if  message.author.id in user :
        
        CHANNEL_ID = message.channel.id
        CHANNEL = bot.get_channel(CHANNEL_ID) #CHANNEL_ID = le message dans le bon channel
        await CHANNEL.send(random.choice(AutoR)) # Message récup de la Liste de message
        print("Emoji Send") # Vérification  
# Fermeture de la boucle    
#    MSG = message.content
#    if  MSG == "stop" in user is True :
#        async def skip():
#        print("break")
#    


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
#                  COMING SOON                    #
###################################################

bot.run("ODQyMDkxODI3OTA4OTY4NDc3.YJwRIQ.IOckQmLlgoR9BJq391CVZOYHUbo")