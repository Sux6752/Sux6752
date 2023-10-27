import telebot
#from telebot import types
bot=telebot.TeleBot("6980649881:AAFVwmGatEDeqK6sYfe1h_CSNHXisertdj0")

@bot.message_handler(commands=['start'])
def start(message, res = False):
    # a = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # q =types.KeyboardButton("Test#1")
    # k =types.KeyboardButton("Test#2")
    # a.add("Тест#1")
    bot.send_message(message.chat.id, "Тест 1 - сделан как и тест 2 в 19:30", "У меня есть кошки", message.text)

@bot.message_handler(content_types=['text'])
def handle_text(message):

    bot.send_message(message.chat.id,"Test",message.text)
if __name__== '__main__':
    bot.polling(none_stop = True, interval=0)

