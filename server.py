from flask import Flask, request
from waitress import serve
from threading import Thread
from replit import db
import os

app = Flask(__name__)

@app.route('/')
def home():
  return "BordBot funcionando!"

@app.route(f'/mensagem/{os.getenv("MENLINK")}', methods=['GET', 'POST'])
def form():
  # Receber o valor do formulário
  if request.method == 'POST':
    db["mensagem-bot"] = request.form['mensagem']
    return f"Mensagem do bot definida para {request.form['mensagem']}"

  # Servir a página estática
  else:
    return app.send_static_file('mensagem.html')

def run():
  serve(app, host="0.0.0.0", port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()