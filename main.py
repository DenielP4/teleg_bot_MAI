import telebot
from telebot import types

bot = telebot.TeleBot('-_-')

name = ''
city = ''
email = ''
phone_number = ''
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton('Я хочу поступить!')
    markup.add(btn)
    send_mess = f"<b>Привет, друг!\nВас приветствует помощник с поступлением в МАИ!</b>!\nНажмите на кнопку для дальнейшей работы!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "я хочу поступить!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как поступить?')
        btn2 = types.KeyboardButton('Личный кабинет')
        btn3 = types.KeyboardButton('Документы для поступления')
        btn4 = types.KeyboardButton('Даты поступления')
        btn5 = types.KeyboardButton('Экзамены')
        btn6 = types.KeyboardButton('Хочу стать пилотом')
        # btn7 = types.KeyboardButton('Оставить заявку')
        btn8 = types.KeyboardButton('Контакты')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8)
        final_message = "Отлично, ты уже на пути: <b>стать студентом МАИ</b>!\nВыбери то, что тебя больше всего интересует!"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "контакты":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Почта МАИ", callback_data='email')
        item2 = types.InlineKeyboardButton("Сайт МАИ", callback_data='web')
        item3 = types.InlineKeyboardButton("Telegram-контакт", url="https://t.me/mai_sng")
        item4 = types.InlineKeyboardButton("WhatsApp-контакт", url="https://wa.me/+79685355895")
        markup.add(item1, item2, item3, item4)
        final_message = f"<b>С нашими сотрудниками международного отдела можно связаться:</b>"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "как поступить?":
        final_message = f"<b>Для того, чтобы поступить в МАИ необходимо выполнить 5 простых шагов:</b>\n" \
                        f"1.	Выбрать направление подготовки, на которое Вы хотите поступать. Ознакомиться со всеми направлениями можно на сайте: https://priem.mai.ru/bachelor/programs\n" \
                        f"2.	Зарегистрировать личный кабинет и подать заявку на поступление. Регистрация откроется 18 июня. В заявке можно указывать до 5 направлений подготовки. " \
                        f"Прием документов на бюджет продлится до 9 июля, а на платное до 13 августа. Страница личного кабинета: lk.mai.ru\n" \
                        f"3.	Сдать экзамены на выбранные Вами направления подготовки. После того, как Ваша заявка будет одобрена, Вам сообщат о расписании экзаменов и проведут тест связи.\n\n" \
                        f"На бюджет нужно сдать <b>3 экзамена</b> (русский+математика+предмет по выбору), на платное обучение можно сдать два экзамена (математика+предмет по выбору).\n" \
                        f"Экзамены пройдут дистанционно: <b>11.07-24.07</b> и <b>14.08-17.08</b> - дополнительно на платное."
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "экзамены":
        final_message = f"<b>Посмотреть какие экзамены необходимо сдавать на каждое направление Вы можете тут:</b> https://priem.mai.ru/bachelor/programs/\n\n" \
                        f"<b>Материалы для подготовки:</b> https://priem.mai.ru/bachelor/tests/#about\n\n" \
                        f"<b>А также у нас есть видеоразбор экзаменационных заданий:</b> https://www.youtube.com/playlist?list=PL6zFn9PtV5nfdnjdhk2zykwTJ0499qOtU\n\n" \
                        f"<b>Экзамены сдаются только один раз!</b> " \
                        f"Если Вы подаете заявление на бюджет, но по баллам не проходите, то можно подать заявление на платное. Если Вы подаете заявление сразу на платное, то потом подать заявление на бюджет уже нельзя. "
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "хочу стать пилотом":
        final_message = f"Если Вы хотите быть летчиком, то должны сказать, что в МАИ нет такого направления подготовки. Однако у нас есть три направления, на которых осуществляется летная практика у студентов на 3 или 4 курсе. Студенты 1 семестр знакомятся с оборудованием на пилотажных стендах. Те, кто успешно сдает зачет по данной" \
                        f" дисциплине, проходят летнюю практику на нашем аэродроме, на реальных самолетах.\n\nДанная практика есть на следующих направлениях:\n" \
                        f"\t24.03.03 Баллистика и гидроаэродинамика\n" \
                        f"\t24.03.04 Авиастроение\n" \
                        f"\t24.05.07 Самолето- и вертолетостроение\n" \
                        f"Вы можете ознакомиться с этими направлениями на сайте: https://priem.mai.ru/bachelor/programs/\n\n" \
                        f"После окончания вы получите документ о высшем образовании по специальности инженер. Далее вы сможете пойти учиться в летное училище, там вам перезачтут образовательные дисциплины, которые вы изучали в МАИ," \
                        f" таким образом для вас сократится срок обучения в училище и вам останется только набрать летные часы там.\n\n" \
                        f"Если Вас интересует такой вариант вашей траектории обучения, то мы расскажем подробнее как поступить на это направление в МАИ."
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "даты поступления":
        final_message = f"<b>Сроки приема: </b>\n" \
                        f"<i>18 июня</i> - начало приема документов\n" \
                        f"<i>10 июля</i> - Окончание приема документов на бюджет\n" \
                        f"<i>11 – 24 июля</i> – экзамены на бюджет\n" \
                        f"<i>24 июля</i> - завершение приема документов на бюджет по ЕГЭ\n" \
                        f"<i>3 августа</i> - завершение приема согласий на зачисление на бюджет\n" \
                        f"<i>5 августа</i> – приказ о зачислении на бюджет\n" \
                        f"<i>13 августа</i> - завершение приема документов на платное для иностранных граждан\n" \
                        f"<i>14 - 17 августа</i> – экзамены на платное для иностранных граждан\n" \
                        f"<i>31 августа</i> – приказ о зачислении на платное"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "документы для поступления":
        final_message = f"<b>Для граждан Республики Казахстан, Республики Таджикистан, Республики Беларусь, Республики Кыргызстан: </b>\n" \
                        f"- Паспорт + нотариально заверенный перевод на русский язык\n" \
                        f"- Документ об образовании + нотариально заверенный перевод на русский язык\n\n" \
                        f"<b>Для граждан всех остальных стран необходимо дополнительно предоставить:</b>\n" \
                        f"- Свидетельство о рождении + нотариально заверенный перевод на русский язык\n" \
                        f"- Свидетельство о рождении родителя + нотариально заверенный перевод на русский язык\n" \
                        f"- Паспорт родителя + нотариально заверенный перевод на русский язык\n" \
                        f"- Документ подтверждающий смену фамилии (при необходимости)\n" \
                        f"- Заявление (форма 49). Это заявление вы видите ниже. Пожалуйста, заполните в соответствии с образцом."
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        doc1 = open("forma_49_obrazec.pdf", 'rb')
        bot.send_document(message.chat.id, doc1)
        doc2 = open("forma_49_sootechestvennik.pdf", 'rb')
        bot.send_document(message.chat.id, doc2)
    elif get_message_bot == "личный кабинет":
        final_message = f"<b>Как заполнять личный кабинет: </b>\n" \
                        f"- Все поля в личном кабинете необходимо заполнять строго на русском языке и в соответствии с нотариально заверенным переводом на русский язык\n" \
                        f"- В строке «Регистрация» необходимо указать адрес постоянной прописки. Если Вы не находите в справочнике свой адрес, то необходимо поставить галочку «свободный ввод» и ввести адрес от руки. (Не нужно ставить галочку в разделе «Без определенного места жительства» \n" \
                        f"- Обязательно указывайте верный номер телефона, иначе мы не сможем с Вами связаться \n" \
                        f"- В личном кабинете Вам будут доступны для скачивания 3 формы заявления. Их необходимо скачать, заполнить, подписать, отсканировать и загрузить обратно в личный кабинет \n" \
                        f"- При выборе перечня вступительных испытаний в графе «Баллы» - ничего не указывайте или поставьте «0». В этом разделе позднее Вы увидите результаты своих экзаменов\n" \
                        f"- Лица без гражданства в графе «Гражданство» указывают страну постоянного проживания \n" \
                        f"- После заполнения всех полей обязательно нажмите кнопку «Отправить». \n" \
                        f"Модератор отсмотрит заявку и, если что-то не так, вернет на доработку с комментариями. "
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "оставить заявку":
        final_message = f"<b>Для того, чтобы оставить заявку, Вы должны ввести некоторую информацию о себе!</b>\n" \
                        f"Введите Ваше ФИО:"
        bot.send_message(message.from_user.id, final_message, parse_mode='html')
        bot.register_next_step_handler(message, reg_name)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как поступить?')
        btn2 = types.KeyboardButton('Личный кабинет')
        btn3 = types.KeyboardButton('Документы для поступления')
        btn4 = types.KeyboardButton('Даты поступления')
        btn5 = types.KeyboardButton('Экзамены')
        btn6 = types.KeyboardButton('Хочу стать пилотом')
        btn7 = types.KeyboardButton('Оставить заявку')
        btn8 = types.KeyboardButton('Контакты')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        final_message = "Ой ой ой, что-то пошло не так!"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'email':
                final_message = f"<b>Почта для работы с абитуриентами:</b> sng@mai.ru"
                bot.send_message(call.message.chat.id, final_message, parse_mode='html')
            elif call.data == 'web':
                final_message = f"<b>Официальный сайт для абитуриентов:</b> priem.mai.ru"
                bot.send_message(call.message.chat.id, final_message, parse_mode='html')
            elif call.data == 'yes':
                final_message = f"Спасибо за регистрацию!"
                bot.send_message(call.message.chat.id, final_message, parse_mode='html')
            elif call.data == 'no':
                final_message = f"Давайте попробуем еще раз!"
                bot.send_message(call.message.chat.id, final_message, parse_mode='html')
                bot.send_message(call.message.chat.id, "Введите Ваше ФИО: ")
                bot.register_next_step_handler(call.message, reg_name)

    except Exception as e:
        print(repr(e))

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Введите страну проживания:")
    bot.register_next_step_handler(message, reg_city)

def reg_city(message):
    global city
    city = message.text
    bot.send_message(message.from_user.id, "Введите Ваш адрес электронной почты:")
    bot.register_next_step_handler(message, reg_email)

def reg_email(message):
    global email
    email = message.text
    bot.send_message(message.from_user.id, "Введите Ваш контактный телефон:")
    bot.register_next_step_handler(message, reg_phone_number)

def reg_phone_number(message):
    global phone_number
    phone_number = message.text
    markup = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton("Да", callback_data='yes')
    key2 = types.InlineKeyboardButton("Нет", callback_data='no')
    markup.add(key1, key2)
    final_massage = f"<b>Проверка введенных данных!</b>\n" \
                    f"Ваше ФИО: " + name + f"\n" \
                    f"Ваша страна проживания: " + city + f"\n" \
                    f"Ваш элетронный адрес: " + email + f"\n" \
                    f"Ваш номер телефона: " + phone_number
    bot.send_message(message.from_user.id, final_massage, parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)