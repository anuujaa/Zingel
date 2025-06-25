# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ContextTypes,
)
from config import BOT_TOKEN

# /start command ka handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot. Send 'I love u' to get a response! 😊")

# Text message ka handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == "i love u":
        # Button ke saath response
        keyboard = [[InlineKeyboardButton("I love u too! 💖", callback_data="love_response")]]
        reply_markup = InlineKeyboardMarkup(keyboard)  # Fixed: Corrected variable name and usage
        await update.message.reply_text("I love u too! 😘", reply_markup=reply_markup)

# Button click ka handler
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Callback query ko acknowledge
    await query.message.reply_text("Aww, you're so sweet! 😊")

def main():
    # Bot application initialize
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers add
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Bot start
    print("Bot started...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
