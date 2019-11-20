import telebot
from logging import DEBUG
telebot.logger.setLevel(DEBUG)
API_TOKEN = '973214590:AAGt1CjZEARL0pIT7zFdexk05CL53fYi5YA'

if API_TOKEN == "":
    exit("Inserire un token")

bot = telebot.TeleBot(API_TOKEN)

i = 0

@bot.message_handler(commands=["start"])
def start(message):
    text = 'Hi, the  command are: \n \t /pressButton \n \t /sum x y \n \t /help'
    bot.send_message(message.from_user.id, text)

@bot.message_handler(commands=["help"])
def start(message):
    text = 'The  command are: \n \t /pressButton \n \t /sum x y'
    bot.send_message(message.from_user.id, text)

@bot.message_handler(commands=["pressButton"])
def mex1(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')
    )
    bot.send_message(message.chat.id, 'Click on the currency of choice:', reply_markup=keyboard)

@bot.message_handler(commands=["get-USD"])
def mex2(message):
    bot.send_message(message.from_user.id, 'me')

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data.startswith('get-'):
       get_ex_callback(query)

def get_ex_callback(query):
   bot.answer_callback_query(query.id)
   pressed = query.data[4:]
   bot.send_message(query.from_user.id, pressed)

@bot.message_handler(commands=["sum"])
def mex(message):
    number = message.text.replace('/sum ', '')
    number = number.split(' ')
    try:
        ret = int(number[0]) + int(number[1])
        bot.send_message(message.from_user.id, str(ret))
    except:
        bot.send_message(message.from_user.id, 'You must tipe the right command: \n /sum number1 number2')

@bot.message_handler(func = lambda message: message.text)
def echo(message):
    bot.send_message(message.from_user.id, message.text)

try:
    bot.polling()
except:
    print("Hai staccato la connessione, vero?")