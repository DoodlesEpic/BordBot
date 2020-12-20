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

# A key deve estar contida na mensagem para ser escolhida uma resposta
respostas = {
  "bord": ["TÁ!!!", "TÁ", "bruno?", "nÃO", "não", "fingindo", "parou", "morre aqui", "melhor não"],
  "brun": ["amiguin?", "amigo", "melhor não", "taborda"],
  "11": ["11 é desconhecido"],
  "12": ["12 é fitness"],
  "13": ["13 é petista"],
  "0": ["0 é guardião supremo"],
  "1": ["1 é normal"],
  "2": ["2 é bolinador"],
  "3": ["3 é bom"],
  "4": ["4 é x"],
  "5": ["5 é guardião supremo"],
  "6": ["6 NAAAHHHHHH CHAMA O GUARDIÃO"],
  "7": ["7 é amigo, mas já foi pior"],
  "8": ["8 é criador"],
  "9": ["9 é amarelo"],
  "10": ["10 é médico"],
}

# A mensagem deve ser exatamente igual a key para ser escolhida uma resposta
respostasExatas = {
  "ta": ["borda"],
  "tá": ["borda"],
  "book": ["writer"],
  "pls boobs": ["punheteiro", "doente", "lek vai pesquisar na internet wtf", "não", "boobs", "de homem?"],
}

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

  # Encontrar substrings em mensagens enviadas
  for key in respostas:
    if key in mensagem:
      return await message.channel.send(random.choice(respostas[key]))

  # Encontrar mensagens que são exatamente iguais aos triggers
  if mensagem in respostasExatas:
    return await message.channel.send(random.choice(respostasExatas[mensagem]))

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