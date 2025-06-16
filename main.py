from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === CONFIGURAÇÕES DO BOT ===
TOKEN = "7574989089:AAEIh-WWopRV_r-wlTJQp9sYW2QusFnoVg8"
GRUPO_ID = -1002733593206

# === MANTÉM O BOT ONLINE NO KOYEB ===
app_web = Flask('')

@app_web.route('/')
def home():
    return "✅ Bot Telegram online via Koyeb!"

def run():
    app_web.run(host='0.0.0.0', port=8080)

def manter_online():
    t = Thread(target=run)
    t.start()

# === COMANDOS DO BOT ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! 👋 Estou online 24h com Koyeb!")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot desenvolvido por Luiz Filipe para o grupo!")

# === MENSAGENS NO GRUPO ===
async def responder_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id == GRUPO_ID:
        texto = update.message.text
        await update.message.reply_text(f"📩 Você disse: {texto}")

# === INICIALIZA O BOT ===
if __name__ == '__main__':
    manter_online()

    app = ApplicationBuilder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))

    # Responde texto (exceto comandos)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensagem))

    app.run_polling()
