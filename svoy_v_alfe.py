import telebot
bot = telebot.TeleBot('7123334264:AAG-4DK5u3HA903dv7WieGo4gPbsD53HttE')
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)