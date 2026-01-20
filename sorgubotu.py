import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# TOKEN ARTIK ORTAM DEĞİŞKENİNDEN ALINIYOR
TOKEN = os.getenv("TOKEN")

BASE_TEXT = (
    "🚫 Bot şu an aktif değil!\n\n"
    "🤖 Beni çalıştırmak için aşağıdaki kanallara katıl 👇\n\n"
)

async def animasyonlu_mesaj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Kanal 1", url="https://t.me/+-XdwcSMYZecwOGFk")],
        [InlineKeyboardButton("📢 Kanal 2", url="https://t.me/+juWCPJr2f5c4NmNk")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = await update.message.reply_text(
        BASE_TEXT + "⏳ Onay bekleniyor.",
        reply_markup=reply_markup
    )

    for dots in [".", "..", "..."]:
        await asyncio.sleep(1)
        await message.edit_text(
            BASE_TEXT +
            f"⏳ Onay bekleniyor{dots}\n\n"
            "🔍 Yetkililer tarafından inceleniyor.\n"
            "🙏 Lütfen sabırla bekle.",
            reply_markup=reply_markup
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", animasyonlu_mesaj))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, animasyonlu_mesaj))

    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()

