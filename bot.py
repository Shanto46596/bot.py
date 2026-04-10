import telebot

TOKEN = "8654187898:AAGF-3uu5yh4u62JhugevIu_VzcMisw9V2w"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Hello! আমি তোমার Render bot")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "তুমি লিখেছো: " + message.text)

bot.infinity_polling()
