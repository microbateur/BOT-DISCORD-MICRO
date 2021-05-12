import discord
from discord.ext import commands
import random
import time
import asyncio
import youtube_dl

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
#    


###################################################
#                    MUSIQUE                      #
###################################################


# Launch
musics = {}
ytdl = youtube_dl.YoutubeDL()

# Initialisation
class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

# Les Commandes
@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)


###################################################
#                  COMING SOON                    #
###################################################

bot.run("ODQyMDkxODI3OTA4OTY4NDc3.YJwRIQ.IOckQmLlgoR9BJq391CVZOYHUbo")