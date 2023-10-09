import discord
import os
import random

from discord.ext import commands

from fonksiyonlar import *



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()                          #bota komut ekliyoruz.
async def para(ctx):  #ctx i unutma     #discordda botumuzu nasıl çağıracağız. ismini girin.
    await ctx.send(yazi_tura())         #çalıştırılacak fonksiyon parantez içine bak.


@bot.command()
async def sifre(ctx, sifre_uzunlugu = 15):
    await ctx.send(gen_pass(sifre_uzunlugu))

@bot.command()
async def emoji(ctx):
    await ctx.send(emoji_olusturucu())


@bot.command()
async def resim(ctx):
    with open('m2\\m2l1\\images\\resim2.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def rastgeleresim(ctx):
    resimler = os.listdir("m2\m2l1\images")
    resim = random.choice(resimler)

    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'm2\m2l1\images\{resim}', 'rb') as f:
            picture = discord.File(f)

   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


oneriler = [
    "nasa benim hedef kitlem. uzaydaki çöpler benim sorunum. uzay mekikleri arasına balık ağı dizilir. daha sonra çöpler toplanır ve mekiklerle dünyaya indirilir. Bu sayede çok fazla miktarda bir geri dönüşüm sağladık.",
    "turmepa benim hedef kitlem.tuzlu suyun tatlı suya çevirme. bütün dünyadaki arıtma makinelerini birleştirip mega arıtma makinesi yapıp tuzlu suyun yüzde 50sini tatlı suya çevirmek.kalan balıkları da yeriz."
]


@bot.command()
async def banafikirver(ctx):
    await ctx.send(random.choice(oneriler))


bot.run()
