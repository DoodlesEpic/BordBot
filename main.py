import asyncio
import discord
import os
import random
import traceback
from keepalive import keep_alive
from crontab import CronTab

import logging
logging.basicConfig(level=logging.INFO)

client = discord.Client()
respostas = ["TÁ!!!", "TÁ", "Bruno?", "NÃO", "Não", "Fingindo", "Parou", "Morre aqui"]

# Configurar cronograma ao inicializar o bot
@client.event
async def on_ready():
  print(f"BordBot inicializado como {client.user}");
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="333"))

  # Enviar a mensagem 333 todas as 3:33
  try:
    interval = "33 6,18 * * *"
    text = "333 CPF mas principalmente PM e PA, L e P, muito feliz, muito amigo, muito carinhoso, roupas, cabelos longos, lisos, bonitos, e sedosos, no ano do futuro DC."

    channel = discord.utils.get(client.get_all_channels(), name='geral')

    print(f'Enviando `{text}` com cronograma `{interval}`')
    client.loop.create_task(falar(interval, channel, text))
  
  except Exception as e: 
    print('Não foi possível configurar o timer 333.')
    print(e)
    traceback.format_exc()

# Responder a mensagens enviadas em qualquer canal
@client.event
async def on_message(message):
  # Não responder a mensagens enviadas pelo própio bot
  if message.author == client.user:
    return

  mensagem = message.content.lower()

  if "bord" in mensagem:
    await message.channel.send(random.choice(respostas))

  elif mensagem == "ta":
    await message.channel.send("borda")

  elif mensagem == "book":
    await message.channel.send("writer")

# Utilizado para enviar a mensagem programado no cronograma
async def falar(interval, channel, text):
  await client.wait_until_ready()
  cron = CronTab(interval)

  while True:
    await asyncio.sleep(cron.next())

    try:
      print(f"Enviando {text} para {channel}")
      await channel.send(text)

    except Exception as e: 
      print(f'Não deu pra enviar `{text}` para `{channel}` :(')
      print(e)

keep_alive()
client.run(os.getenv("TOKEN"))