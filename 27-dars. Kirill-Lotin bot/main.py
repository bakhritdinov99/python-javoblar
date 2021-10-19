from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("2070189183:AAF7vhot4tA71lQ0qdU1Z9IkNpiOrxGtk9U", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Matn kiriting ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()

matn = input(">>>")
