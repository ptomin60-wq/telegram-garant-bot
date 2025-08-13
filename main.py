from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'YOUR_BOT_TOKEN_HERE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привіт! Я бот-гарант. Введи /newdeal для початку нової угоди.")

async def new_deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✍️ Створи угоду:\n\n/deal [сума] [@покупець] [@продавець]")

async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 3:
        await update.message.reply_text("⚠️ Неправильний формат. Приклад: /deal 500 @buyer @seller")
        return
    amount, buyer, seller = args
    await update.message.reply_text(
        f"✅ Угода створена:\n💰 Сума: {amount}\n👤 Покупець: {buyer}\n👤 Продавець: {seller}\n\nОчікуємо підтвердження..."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newdeal", new_deal))
app.add_handler(CommandHandler("deal", deal))

app.run_polling()
