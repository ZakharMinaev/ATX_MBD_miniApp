import telebot
from telebot import types

import os

token = os.getenv("TG_BOT")
bot = telebot.TeleBot(token)
APP_URL = "https://zakharminaev.github.io/ATX_MBD_miniApp/"

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем специальную кнопку для открытия Mini App
    web_app = types.WebAppInfo(APP_URL)
    btn = types.KeyboardButton("Открыть калькулятор", web_app=web_app)
    markup.add(btn)
    
    bot.send_message(
        message.chat.id, 
        "Нажмите на кнопку ниже, чтобы открыть калькулятор:", 
        reply_markup=markup
    )

bot.polling(none_stop=True)

