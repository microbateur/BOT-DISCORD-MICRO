import discord
from discord.ext import commands
import random
import time
from discord.ext.commands.bot import when_mentioned
from discord.ext.commands.core import command
import asyncio
import emoji
from discord.user import User

#prefix
bot = commands.Bot(command_prefix='!')

###################################################
#                     DEBUT                       #
###################################################


print("LAUNCH")


###################################################
#                  AUTO REPONSE                   #
###################################################


#Valeurs Initiales du STOP
STOPPED = False
STOP_COUNT = 0
#
@bot.event
async def on_message(message):
#Valeur de Base pour le STOP
    global STOPPED
    global STOP_COUNT
# Valeur de Base des Messages
    global CS_ID
    global CS
    C_ID = message.channel.id #id du message
    C = bot.get_channel(C_ID) #Localisation du message
# Liste de message et d'émoji
    Ewink = emoji.emojize(":wink:")
    EGulag = bot.get_emoji(799687664060203028)
    EFNews = bot.get_emoji(802274654005755935)
    EPOWA = bot.get_emoji(797821182824022046)
    AutoM = ["Mais NON!","Ah Oui " + str(Ewink) ,"Genre","Okem Cool " + str(EGulag),"Alors peut-être", "Attention " + str(EFNews)]
    MSG = message.content
# User
    user = [683018314611687549,226741480595652608,584125468773711896,107749538319601664,180724665042337793,259611405643284483,252436885568225281] #Id de la cible
    user1 = [492278387038093312] #Id de la cible Emoji
# Auto Réaction
    if  message.author.id in user1:
        await message.add_reaction("👉")
        await message.add_reaction("👌")
        print("Emoji Send") # Vérification  
# Auto Message
    #Si le message contient STOP on remet le compteur à 0
    if "stop" in MSG :
        STOPPED = True
        STOP_COUNT = 0
        await C.send("Auto Message est arrêté :sleeping:")
    #Si STOPPED est égale à vrai en liaison avec MSG = "stop" on met un compteur +1 à chaque passage
    if STOPPED == True:
        STOP_COUNT = STOP_COUNT + 1
        if STOP_COUNT == 29:
            await C.send("Auto Message est de retour "+ str(EPOWA)) #Message avant lancement
        if STOP_COUNT > 30:
            STOPPED = False
            STOP_COUNT = 0
    if  message.author.id in user and STOPPED == False:
        await C.send(random.choice(AutoM)) #Message Random récupéré de la liste AutoM
        print("Message Send") # Vérification  

    await bot.process_commands(message) #fin de bot event
#    
      

###################################################
#                  FERMETURE                      #
###################################################


#fermeture du bot
@bot.command()
async def close(ctx) :
    await bot.close()
    time.sleep(1)
    print("Bot Closed")
 

###################################################
#                  COMING SOON                    #
###################################################

bot.run("ODQyMDkxODI3OTA4OTY4NDc3.YJwRIQ.IOckQmLlgoR9BJq391CVZOYHUbo")