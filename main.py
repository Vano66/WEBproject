import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

f, h, d, r = 0, 0, 0, 0


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
    btn4 = types.KeyboardButton("Романтичный")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
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
    elif message.text == "Романтичный":
        result(4)
        bot.send_message(message.chat.id, "Результаты!", reply_markup=a)
        end(message)


def round_1(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Погрузиться в другой мир")
    btn2 = types.KeyboardButton("Наслаждение от расследований преступлений")
    btn3 = types.KeyboardButton("Почуствовать ужас")
    btn4 = types.KeyboardButton("Прожить первую любовь")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
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
    elif message.text == "Прожить первую любовь":
        result(4)
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
    elif res == 4:
        global r
        r += 1


def end(message):
    global f, h, d, r
    if f == 2:
        bot.send_message(message.chat.id, "Вам определенно понравиться фантастика")
        f, h, d, r = 0, 0, 0, 0

    elif h == 2:
        bot.send_message(message.chat.id, "Вам определенно понравиться хоррор")
        f, h, d, r = 0, 0, 0, 0

    elif d == 2:
        bot.send_message(message.chat.id, "Вам определенно понравиться детективы и триллеры")
        f, h, d, r = 0, 0, 0, 0
    elif r == 2:
        bot.send_message(message.chat.id, "Вам определенно понравиться романы и сборники стихов")
        f, h, d, r = 0, 0, 0, 0

    else:
        bot.send_message(message.chat.id, "Вам определенно понравиться любая наша книга")
        f, h, d, r = 0, 0, 0, 0
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Давай тест")
    btn2 = types.KeyboardButton("Давай про жанры")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Пройти тест еще раз или прочитать про жанры литературы?", reply_markup=markup)
    bot.register_next_step_handler(message, next_round)


def next_round(message):
    if message.text == "Давай тест":
        round_1(message)
    elif message.text == "Давай про жанры":
        janr(message)


def janr(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Фантастика")
    btn2 = types.KeyboardButton("Детектив")
    btn3 = types.KeyboardButton("Хоррор")
    btn4 = types.KeyboardButton("Романтика")
    btn5 = types.KeyboardButton("Узнать про авторов, пишущих в этих жанрах")
    btn6 = types.KeyboardButton("Обратно")
    markup.row(btn1, btn2, btn6)
    markup.row(btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Про какой жанр вам интересно узнать?", reply_markup=markup)
    bot.register_next_step_handler(message, janr1234)


def janr1234(message):
    if message.text == "Фантастика":
        bot.send_message(message.chat.id,
                         "Фантастика — жанр, объединяющий художественные"
                         " произведения, в которых повествуется о событиях,"
                         " мирах и героях, нарушающих границы реальности. Фантастика рассказывает о том,"
                         " что находится за гранью реальности, и строится на фантастическом допущении.")
        janr(message)
    elif message.text == "Детектив":
        bot.send_message(message.chat.id,
                         "Детектив — жанр остросюжетной литературы, который повествует"
                         " о расследовании загадочного случая, чаще всего преступления.")
        janr(message)
    elif message.text == "Хоррор":
        bot.send_message(message.chat.id,
                         "Хоррором называют жанр в кино и литературе, который стремится"
                         " напугать зрителей и читателей. Этот термин происходит от латинского"
                         " слова horror — ужас, оцепенение. Как правило, произведения этого"
                         " жанра посвящены чудовищам, потусторонним силам и различным жутким событиям.")
        janr(message)
    elif message.text == "Романтика":
        bot.send_message(message.chat.id,
                         "Романтизм — это направление в литературе, которое возникло в конце XVIII"
                         " века (1790-е годы) в Западной Европе, а затем появилось и в России. От других"
                         " направлений романтизм отличается идеальным миром и борьбой лирического героя"
                         " с обществом.1 сент. 2023 г.")
        janr(message)
    elif message.text == "Узнать про авторов, пишущих в этих жанрах":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Фантастический автор")
        btn2 = types.KeyboardButton("Автор детектив")
        btn3 = types.KeyboardButton("Страшный автор")
        btn4 = types.KeyboardButton("Романтичный автор")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, "Про какой жанр вам интересно узнать?", reply_markup=markup)
        bot.register_next_step_handler(message, avtor)

    elif message.text == "Обратно":
        start(message)


def avtor(message):
    if message.text == "Фантастический автор":
        bot.send_message(message.chat.id,
                         "Дж. Р. Р. Толкин (полное имя — Джон Рональд Руэл Толкин / John Ronald Reuel Tolkien) (1892-1973)"
                         " — английский писатель. Известность ему принесли книги «Хоббит или туда и обратно» и «Властелин Колец»,"
                         " хотя он опубликовал и много других произведений. После его смерти на основе сохранившихся записей"
                         " была издана книга «Сильмариллион»; впоследствии были опубликованы другие его тексты, они продолжают"
                         " публиковаться и в настоящее время. ")
        janr(message)
    elif message.text == "Автор детектив":
        bot.send_message(message.chat.id,
                         "Артур Конан Дойл (1859 — 1930) Популярные романы: «Собака Баскервилей», «Этюд в багровых тонах», «Знак четырех» "
                         "Популярный персонаж: Шерлок Холмс, лондонский частный детектив, биохимик, обладает разносторонними талантами, отлично"
                         " знает анатомию, химию, медицину, убежденный холостяк, сильно зависимый курильщик, употребляет кокаин внутривенно"
                         " при полном отсутствии интересных преступлений.")
        janr(message)
    elif message.text == "Страшный автор":
        bot.send_message(message.chat.id,
                         "Стивен Кинг – американский писатель, создающий ужасы, триллеры, фантастику, фэнтези, мистические"
                         " романы и драмы, обладатель премий Брэма Стокера и О. Генри, Всемирной премии фэнтези, наград Британского"
                         " общества фэнтези и Канадской ассоциации книготорговцев, медали Национального фонда книг за выдающийся"
                         " вклад в американскую литературу, звания Великого Магистра от Американских писателей-мистиков,"
                         " Национальной медали США в области искусств с формулировкой «за сочетание захватывающих историй"
                         " с анализом человеческой натуры».")
        janr(message)
    elif message.text == "Романтичный автор":
        result(4)
        bot.send_message(message.chat.id,
                         "Уильям Шекспир – английский поэт, один из величайших англоязычных писателей и драматургов мира. "
                         "Уильям Шекспир родился 26 апреля 1564 года в многодетной состоятельной семье, где был третьим ребенком"
                         " среди семи братьев и сестер. Будущий литератор сначала посещал грамматическую школу Стратфорда,"
                         " а затем продолжил обучение в школе короля Эдуарда Шестого. Когда юноше исполнилось восемнадцать,"
                         " он женился и обзавелся тремя детьми.")
        janr(message)


bot.polling(none_stop=True)
