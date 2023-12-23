import telebot
from telebot import types
bot = telebot.TeleBot("6915179867:AAENgjxq9T6XSpRC_4H2wl9sUsjhZjjvMTs")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выбирите жанр музыки - ')
    print(message)
if __name__== '__main__':
    bot.polling(none_stop = True, interval=0)