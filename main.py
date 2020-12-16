import discord
import os
import random
from keepalive import keep_alive

import logging
logging.basicConfig(level=logging.INFO)

client = discord.Client()
channel = ""
respostas = ["TÁ!!!", "TÁ", "Bruno?", "NÃO", "Não", "Fingindo", "Parou", "Morre aqui"]

@client.event
async def on_ready():
  print(f"BordBot inicializado como {client.user}");

@client.event
async def on_message(message):
  # Não responder a mensagens enviadas pelo própio bot
  if message.author == client.user:
    return

  if "bord" in message.content:
    channel = message.channel
    await channel.send(random.choice(respostas))

keep_alive()
client.run(os.getenv("TOKEN"))