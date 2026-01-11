import telebot
from telebot import types

bot = telebot.TeleBot("8565768319:AAFR9zCD1I0Vii0EydKuoscgTJX7x7OwWdg")

# Словарь для хранения данных пользователей
user_data = {}


@bot.message_handler(commands=["start", "calculate"])
def start(message):
    bot.send_message(message.chat.id, "Введите начальный пробег (way1):")
    bot.register_next_step_handler(message, get_way1)


def get_way1(message):
    user_data[message.chat.id] = {"way1": message.text}
    bot.send_message(message.chat.id, "Введите конечный пробег (way2):")
    bot.register_next_step_handler(message, get_way2)


def get_way2(message):
    user_data[message.chat.id]["way2"] = message.text
    bot.send_message(message.chat.id, "Сколько топлива в баке (fuel):")
    bot.register_next_step_handler(message, get_fuel)


def get_way2(message):
    user_data[message.chat.id]["way2"] = message.text
    bot.send_message(message.chat.id, "Сколько топлива в баке (fuel):")
    bot.register_next_step_handler(message, get_fuel)


def get_fuel(message):
    user_data[message.chat.id]["fuel"] = message.text
    bot.send_message(message.chat.id, "Введите норму расхода (norm):")
    bot.register_next_step_handler(message, get_norm)


def get_norm(message):
    try:
        data = user_data[message.chat.id]
        way1 = int(data["way1"])
        way2 = int(data["way2"])
        fuel = float(data["fuel"])
        norm = float(message.text)

        # Ваш алгоритм расчета
        fuelm = (way2 - way1) * norm / 100
        ostatok = fuel - fuelm

        bot.send_message(
            message.chat.id,
            f"Расход составил: {fuelm:.2f} л.\nОстаток в баке: {ostatok:.2f} л.",
        )
    except Exception as e:
        bot.send_message(
            message.chat.id,
            "Ошибка! Пожалуйста, вводите только числа. Попробуйте снова: /calculate",
        )


bot.polling(none_stop=True)
