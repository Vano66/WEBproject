import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

f, h, d = 0, 0, 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Пройти тест")
    markup.row(btn1)
    bot.send_message(message.chat.id, "Вас приветствует Бот для подбора подходящей вам книги", reply_markup=markup)
    bot.register_next_step_handler(message, round_1)


def round_2(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Умный и рассудительный")
    btn2 = types.KeyboardButton("Любознательный и наивный")
    btn3 = types.KeyboardButton("В вечной опасноти")
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, "Какой главный герой больше всего вам понравился", reply_markup=markup)
    bot.register_next_step_handler(message, res_round_2)


def res_round_2(message):
    a = telebot.types.ReplyKeyboardRemove()
    if message.text == "Любознательный и наивный":
        result(1)
        bot.send_message(message.chat.id, "Результаты!", reply_markup=a)
        end(message)
    elif message.text == "Умный и рассудительный":
        result(2)
        bot.send_message(message.chat.id, "Результаты!", reply_markup=a)
        end(message)
    elif message.text == "В вечной опасноти":
        result(3)
        bot.send_message(message.chat.id, "Результаты!", reply_markup=a)
        end(message)


def round_1(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Погрузиться в другой мир")
    btn2 = types.KeyboardButton("Наслаждение от расследований преступлений")
    btn3 = types.KeyboardButton("Почуствовать ужас")
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, "Что вы хотите получить от книги?", reply_markup=markup)
    bot.register_next_step_handler(message, res_round_1)


def res_round_1(message):
    if message.text == "Погрузиться в другой мир":
        result(1)
        bot.send_message(message.chat.id, "Поехали дальше")
        round_2(message)
    elif message.text == "Наслаждение от расследований преступлений":
        result(2)
        bot.send_message(message.chat.id, "Поехали дальше")
        round_2(message)
    elif message.text == "Почуствовать ужас":
        result(3)
        bot.send_message(message.chat.id, "Поехали дальше")
        round_2(message)


def result(res):
    if res == 1:
        global f
        f += 1
    elif res == 3:
        global h
        h += 1
    elif res == 2:
        global d
        d += 1


def end(message):
    if f > h >= d or f > d >= h:
        bot.send_message(message.chat.id, "Вам определенно понравиться фантастика")
    elif h > f >= d or h > d >= f:
        bot.send_message(message.chat.id, "Вам определенно понравиться хоррор")
    elif d > h >= f or d > f >= h:
        bot.send_message(message.chat.id, "Вам определенно понравиться детективы и триллеры")
    else:
        bot.send_message(message.chat.id, "Вам определенно понравиться любая наша книга")


bot.polling(none_stop=True)
