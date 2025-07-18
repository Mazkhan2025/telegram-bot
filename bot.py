from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7607865658:AAGzPdwg6KeIC5YR_sxbTCehqOKD7UiRmoU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات روشنه و داره جواب میده.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("ربات داره اجرا میشه...")
    app.run_polling()

if __name__ == "__main__":
    main()


