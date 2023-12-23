import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot=telebot.TeleBot("6980649881:AAFVwmGatEDeqK6sYfe1h_CSNHXisertdj0")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Весна - коты прилетели")

    bot.send_message(message.chat.id, "Весна - люди прилетели")

    bot.reply_to(message, "опаганамстайл")

@bot.message_handler(commands=['contacts'])
def start(message):

    bot.reply_to(message, "Я Ларисочка Гузеева мне 9999 лет я играю в в самую новую игру - в тетерис")

@bot.message_handler(commands=['photo'])
def start(message):
    photo=open(r"C:\Users\Ученик\Desktop\1.jpg", 'rb')
    bot.send_photo(message.chat.id,photo,"В пОиСкАх НеМо")

@bot.message_handler(commands=['video'])
def start(message):
    video=open(r"C:\Users\Ученик\Desktop\videoplayback.mp4", 'rb')
    bot.send_video(message.chat.id,video,"ФуФлИк")

@bot.message_handler(commands=['delete'])
def start(message):
    bot.delete_message(message.id)

'''@bot.message_handler(commands=['gifs'])
def button_message(message):
    a = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #a = types.ReplyKeyboardMarkup()

    button1 = types.KeyboardButton("Test#1")
# button1 =types.KeyboardButton("Test#1")

    button2 = types.KeyboardButton("Test#2")
# button2 =types.KeyboardButton("Test#2")

    button3 = types.KeyboardButton("Test#3")
    a.add(button1,button2,button3)
    bot.send_message(message.chat.id, 'hello', reply_markup=a)'''

@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона",  url='google.com')
    button_geo = types.KeyboardButton(text="Отправить местоположение", url='google.com')
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id,'<b>TortI</b>', parse_mode='html')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == 'хай':
        bot.send_message(message.chat.id,'<b>TortI</b>', parse_mode='html')
    elif message.text.lower() == 'qbjk':
        bot.send_message(message.chat.id,'28 Ударов ножом!')
    elif message.text.lower() == 'Весна':
        bot.send_message(message.chat.id,'Коты прилетели')


    bot.send_message(message.chat.id,"Test",message.text)



if __name__== '__main__':
    bot.polling(none_stop = True, interval=0)