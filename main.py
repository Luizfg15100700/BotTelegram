from flask import Flask, request
from telegram import Bot, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

app = Flask(__name__)

async def start(update, context):
    # Enviar fotos
    with open("media/foto1.jpg", "rb") as photo1, open("media/foto2.jpg", "rb") as photo2:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(photo1))
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(photo2))

    # Enviar vídeos
    for i in range(1, 4):
        with open(f"media/video{i}.mp4", "rb") as video:
            await context.bot.send_video(chat_id=update.effective_chat.id, video=InputFile(video))

    # Mensagem final
    msg = """
🔥 You're in, baby… but the real game starts after the unlock. 🔥
What you see here? It's just a tease.
The real pleasure? It's hidden behind one click. And it's waiting for you.

💎 Inside:
– Uncensored. Unfiltered. Unforgettable.
– Exclusive content I don’t share anywhere else.
– Daily updates to keep you begging for more...

💋 Don’t just watch. Don’t just wonder.
Unlock now and come taste what you've only dreamed about.

👉 Tap to unlock. I’ll be waiting... wearing nothing but a smile. 😈

👉 https://encr.pw/elarisvip
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

@app.route("/")
def home():
    return "Bot is alive."

def run_bot():
    app_telegram = ApplicationBuilder().token(TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.run_polling()

if __name__ == "__main__":
    run_bot()
