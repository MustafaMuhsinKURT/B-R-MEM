import os
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def resim(ctx):
  
    images = os.listdir("images")

    
    if not images:
        await ctx.send("Resimler klasörü boş!")
        return

  
    img_name = random.choice(images)

    
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("TOKEN BURAYA HOCAM AMA YAZMADIM SIKINTI ÇIKIYO ")
