import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print(f"BordBot inicializado como {client.user}");

@client.event
async def on_message(message):
  # Não responder a mensagens enviadas pelo própio bot
  if message.author == client.user:
    return

  if message.content.startswith("bord"):
    await message.channel.send("TÁ!!!")

client.run(os.getenv("TOKEN"))