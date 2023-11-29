import telebot

bot = telebot.TeleBot("6756892283:AAFUaUlRw-hOVrCaqULb1fDX-Uwg-GCgPEQ")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,"здаров заебал")


@bot.message_handler(commands=['сам ты....'])
def main(message):
    bot.send_message(message.chat.id,"неправда ")

bot.infinity_polling()
