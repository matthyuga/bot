# bot
bot de discord
#_______________________________________________________________________INICIO DEL BOT
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json
DISCORD_TOKEN = 'ODk5ODAyNzAzMzY1MDIxNzY2.YW4Ekg.AdNnNYVrnzmixFPiO2Ez8SBou-A'
#esto es del servidor del discord con el token

#_______________________________________________________________________PREFIJO
bot = commands.Bot(command_prefix='!')
#_______________________________________________________________________

  

#es del bot de dados
#__________________________________________________________________________

#______________________________________________________________________IMPORTAR RANDON

import random
for i in range (1):
#______________________________________________________________________

#_____________________________________________________________________IMAGENES
    imagen1 = 'https://media.discordapp.net/attachments/807091135608258560/900836975999848498/exito.png'
    imagen2 = 'https://cdn.discordapp.com/attachments/807091135608258560/900836977295917126/fracaso.png'

#__________________________________________________________________________EXP DE BOT DISCORD
    @bot.command(name='dadoexito')
    async def tirar(ctx):
     operador1 = random.choice([imagen1 ,imagen2])
     await ctx.send('la tirada salio')
     await ctx.send(operador1)
        

#__________________________________________________________________________ENCENDIDO
bot.run(DISCORD_TOKEN) 
