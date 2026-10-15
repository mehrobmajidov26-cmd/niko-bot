import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8899171018:AAGu2oEL4YCg5M2Z0fSXzloc0aPeIGz9XE8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салом! Ман NIKO AL ҳастам 🔥\n/image - акс месозам")

async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Мисол: /image Mikey on motorcycle")
        return
    await update.message.reply_text(f"Сохта истодаам: {prompt} ⏳")
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=512&height=512&nologo=true&seed={update.message.id}"
    await update.message.reply_photo(photo=url, caption=f"NIKO AL: {prompt}")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Фаҳмидам: {update.message.text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("image", image_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
