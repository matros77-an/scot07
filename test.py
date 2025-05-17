import telebot

BOT_TOKEN = '7907687282:AAG4zMnduWkBxn0V7l1_AyXDkqut1bzfpxA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
