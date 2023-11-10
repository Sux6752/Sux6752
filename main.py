import telebot
from telebot import types
bot=telebot.TeleBot("6980649881:AAFVwmGatEDeqK6sYfe1h_CSNHXisertdj0")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == 'хай':
        bot.send_message(message.chat.id,'<b>TortI</b>', parse_mode='html')
    elif message.text.lower() == 'qbjk':
        bot.send_message(message.chat.id,'28 Ударов ножом!')
    elif message.text.lower() == 'Весна':
        bot.send_message(message.chat.id,'Коты прилетели')


    bot.send_message(message.chat.id,"Test",message.text)
@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])
def star(message):
        # a = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.ReplyKeyboardMarkup()

    button1 = types.KeyboardButton("Test#1")
        # button1 =types.KeyboardButton("Test#1")

    button2 = types.KeyboardButton("Test#2")
        # button2 =types.KeyboardButton("Test#2")

    button3 = types.KeyboardButton("Test#3")

    a.row(button1)
    bot.send_message(message.chat.id,  reply_markup=a)
if __name__== '__main__':
    bot.polling(none_stop = True, interval=0)