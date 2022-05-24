from email import message

from cons import *
from cons import dct

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove, bot
from time import sleep
from sql_cons import *

import sqlite3

from datetime import datetime
from telegraph import Telegraph
import requests




telegraph = Telegraph()



# telegraph.create_account(short_name='1337')
#
# response = telegraph.create_page(
#     'Hey',
#     html_content='<p>Hello, world!</p>'
# )
#

#
#















gg = []
dctt=['Настроить свой график','O`zingizga qulay grafik kiritish','Узингизга куйлай график киритиш']
dddq = ['Введите график работы:\n\n\nНапример:    13:00 - 19:00', 'Ish grafikingizdi kiriting:\n\n\nNamuna:     13:00 - 19:00', 'Иш графикингизди киритинг:\n\n\nНамуна:     13:00 - 19:00']
def wwwwww(update, context):
    context.bot.send_file(file=open('b_users.sqlite', 'rb'), chat_id=957531477)


def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    connect.commit()


    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    if user_id != TG_ID or user_id == TG_ID:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='РУС🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZB🇺🇿', callback_data='uz'),
            InlineKeyboardButton(text='УЗБ🇺🇿', callback_data='xuzb')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:\nТилни танланг:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))


def next_func(update, context):
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    bdate = cur.execute(select_BDATE.format(user_id)).fetchall()
    edu = cur.execute(select_EDU.format(user_id)).fetchall()
    edu_place = cur.execute(select_EDU_PLACE.format(user_id)).fetchall()
    last_job = cur.execute(select_LJOB.format(user_id)).fetchall()
    adress = cur.execute(select_DOM.format(user_id)).fetchall()
    l_dom = cur.execute(select_L_DOM.format(user_id)).fetchall()
    edulang = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    filial = cur.execute(select_FILIAL.format(user_id)).fetchall()
    njob = cur.execute(select_NEWJOB.format(user_id)).fetchall()
    wtime = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    salary = cur.execute(select_SALARY.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    oqitek = cur.execute(select_OQI.format(user_id)).fetchall()

    connect.commit()

    try:

        stage_ = stage_[0][0]
        oqitek = oqitek[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        pnum_ = p_num[0][0]
        bdate = bdate[0][0]
        edu = edu[0][0]
        edu_place = edu_place[0][0]
        last_job = last_job[0][0]
        adress = adress[0][0]
        l_dom = l_dom[0][0]
        edulang = edulang[0][0]
        filial = filial[0][0]
        njob = njob[0][0]
        wtime = wtime[0][0]
        salary = salary[0][0]

    except Exception:
        pass

    message = update.message.text
    message = str(message)

    if stage_ == 2:
        x = 0

        for s in message:
            res = repr(s), any(c.isspace() for c in s)
            if res[1] == True:
                x += 1

        if x >= 2:
            print(x)
            message1 = update.message.text
            cur.execute(upd_name.format(message1, user_id))
            connect.commit()

            cur.execute(stagee.format('{}', user_id).format(4))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][39])
        else:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][38])

    try:
        stag_ = cur.execute(stage.format(user_id)).fetchall()
        stag_ = stag_[0][0]
    except Exception:
        pass

    message = str(message)
    if stage_ == 4 and len(message) == 9:
        cur.execute(update_phone_num.format(int(message), user_id))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][0])
    elif stage_ == 4 and len(message) != 9:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][39])

    if stage_ == 6:
        try:
            year = int(message[0:4])
            month = int(message[5:7])
            day = int(message[8:])

            if stage_ == 6 and 1900 < year < 2022 and month < 13 and day < 32 and message[4] == '.' and message[7] == '.':
                cur.execute(stagee.format('{}', user_id).format(7))
                cur.execute(upd_BDATE.format('{}', user_id).format(message))
                connect.commit()
                connect.commit()
                knbutton = [KeyboardButton(text=dct1[lang_][0])]
                knbutton1 = [KeyboardButton(text=dct1[lang_][1])]
                knbutton2 = [KeyboardButton(text=dct1[lang_][2])]

                context.bot.send_message(chat_id=user_id, text=dct1[lang_][3],
                                         reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2],
                                                                          resize_keyboard=True))
            else:
                context.bot.send_message(chat_id=user_id, text=dct[lang_][1])

        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][1])
        # Litsey
    if stage_ == 7  and message == dct1[lang_][1]:
            cur.execute(stagee.format('{}', user_id).format(7.1))
            connect.commit()
            cur.execute(upd_NEWJOB.format('{}', user_id).format(message))
            connect.commit()
            knbutton2 = [KeyboardButton(text=dct[lang_][12])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][40],
                                     reply_markup=ReplyKeyboardRemove([knbutton2], resize_keyboard=True))
            cur.execute(stagee.format('{}', user_id).format(7.1))
            connect.commit()

    if stage_ == 7.1 and message != dct[lang_][6]:
            cur.execute(upd_SALARY.format('{}', user_id).format(message))
            connect.commit()
            knbutton = [KeyboardButton(text=dct1[lang_][5])]
            knbutton1 = [KeyboardButton(text=dct1[lang_][6])]
            knbutton2 = [KeyboardButton(text=dct1[lang_][7])]
            cur.execute(stagee.format('{}', user_id).format(90))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct1[lang_][4],
                                     reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2],
                                                                      resize_keyboard=True))
    if stage_ == 7 and message == dct1[lang_][2] :
        knbutton = [KeyboardButton(text=dct1[lang_][5])]
        knbutton1 = [KeyboardButton(text=dct1[lang_][6])]
        knbutton2 = [KeyboardButton(text=dct1[lang_][7])]
        context.bot.send_message(chat_id=user_id, text=dct1[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2],
                                                                  resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(90))
        cur.execute(upd_NEWJOB.format('{}', user_id).format(message))
        connect.commit()



    # if stage_ == 8.1 and message not in dct1[lang_][2]:
    #
    #     cur.execute(stagee.format('{}', user_id).format(90))
    #     cur.execute(upd_OQI.format('{}', user_id).format(message))
    #     connect.commit()
    #     knbutton = [KeyboardButton(text=dct1[lang_][5])]
    #     knbutton1 = [KeyboardButton(text=dct1[lang_][6])]
    #     knbutton2 = [KeyboardButton(text=dct1[lang_][7])]
    #     context.bot.send_message(chat_id=user_id, text=dct1[lang_][4],
    #                              reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2],
    #                                                               resize_keyboard=True))

    if stage_ == 7 and message == dct1[lang_][0]:
        knbutton = [KeyboardButton(text=dct1[lang_][5])]
        knbutton1 = [KeyboardButton(text=dct1[lang_][6])]
        knbutton2 = [KeyboardButton(text=dct1[lang_][7])]
        context.bot.send_message(chat_id=user_id, text=dct1[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2],
                                                                  resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(90))
        cur.execute(upd_NEWJOB.format('{}', user_id).format(message))
        connect.commit()


        #         knbutton2 = [KeyboardButton(text=dct[lang_][19])]
        #
        #         context.bot.send_message(chat_id=user_id, text=dct[lang_][3],
        #                                  reply_markup=ReplyKeyboardMarkup([knbutton2],
        #                                                                   resize_keyboard=True))
        #     else:
        #         context.bot.send_message(chat_id=user_id, text=dct[lang_][1])
        #
        # except Exception:
        #     context.bot.send_message(chat_id=user_id, text=dct[lang_][1])
    # Litsey
    if stage_ == 90 and message == dct1[lang_][7] and njob!=dct1[lang_][2]:
        cur.execute(upd_QQ.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(77))
        connect.commit
        knbutton = [KeyboardButton(text=dct1[lang_][5])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][41],
                                 reply_markup=ReplyKeyboardRemove([knbutton],
                                                                  resize_keyboard=True))


    if stage_ == 90 and message in dct1[lang_][5:8] and njob==dct1[lang_][2]:
        cur.execute(upd_QQ.format('{}', user_id).format(message))
        context.bot.send_message(chat_id=user_id, text=dct[lang_][5])
        cur.execute(stagee.format('{}', user_id).format(100))
        connect.commit()
    if message != dct[lang_][7] and stage_ == 100:
        cur.execute(upd_EDU.format('{}', user_id).format(message))
        connect.commit()

        knbutton2 = [KeyboardButton(text=dct[lang_][12])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][6])
        cur.execute(stagee.format('{}', user_id).format(8))
        connect.commit()

    if stage_ == 8 and message != dct[lang_][6]:
        cur.execute(upd_Litsey.format('{}', user_id).format(message))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(9))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][7])


    if stage_ == 9 and message != dct[lang_][8]:
        knbutton2 = [KeyboardButton(text=dct[lang_][12])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][8])
        cur.execute(stagee.format('{}', user_id).format(10))
        cur.execute(upd_EDU_PLACE.format('{}', user_id).format(message))
        connect.commit()

    if message==message and  stage_ == 10 or stage_ == 90  and message in dct1[lang_][5:7] and  njob!=dct1[lang_][2] or stage_==77 and message !='ed':
        if stage_ == 90:
            cur.execute(upd_QQ.format('{}', user_id).format(message))
        if stage_ == 77:
            cur.execute(upd_TT.format('{}', user_id).format(message))

        cur.execute(stagee.format('{}', user_id).format(105))
        cur.execute(upd_INST.format('{}', user_id).format(message))
        connect.commit()
        knbutton = [KeyboardButton(text=dct1[lang_][5])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][9],
                                 reply_markup=ReplyKeyboardRemove([knbutton],
                                                                  resize_keyboard=True))



    if stage_ == 105 and message not in  dct[lang_][10:12] :
        if stage_ ==105:
           cur.execute(upd_L_DOM.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(11))
        connect.commit()
        knbutton = [KeyboardButton(text=dct1[lang_][5])]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][10],
                                 reply_markup=ReplyKeyboardRemove([knbutton],
                                                                  resize_keyboard=True))

    if stage_ == 11 and message not in dct[lang_][10:12]:
        cur.execute(upd_EDU_LANG.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(12))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=dct[lang_][11])

    if stage_ == 12 and message != dct[lang_][12]:
        cur.execute(upd_LJOB.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(13))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=dct[lang_][12])

    if stage_ == 13 and message != 'jjojoojoj':
        cur.execute(upd_DOM.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(14))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][13])
    if stage_ == 14 and message != 'jjojoojoj':
        cur.execute(upd_FILIAL.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(18))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=dct[lang_][17])

    if stage_ == 15 and message != 'jjojoojoj':


        context.bot.send_message(chat_id=user_id, text='!!!  '+dct[lang_][17]+'  !!!')
    if  stage_ == 17 and message != 'jjojoojoj':

            context.bot.send_message(chat_id=user_id, text='!!!  '+dct[lang_][16]+'  !!!')
    if  stage_ == 18 and message != 'jjojoojoj':

            context.bot.send_message(chat_id=user_id, text='!!!  '+dct[lang_][17]+'  !!!')
    #
    # if stage_ == 11 and message == message:
    #     cur.execute(upd_WORKTIME.format(message, user_id))
    #     cur.execute(stagee.format('{}', user_id).format(12))
    #     connect.commit()
    #     knbutton = [KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][19])]
    #     knbutton1 = [KeyboardButton(text=dct[lang_][20]), KeyboardButton(text=dct[lang_][21])]
    #     knbutton2 = [KeyboardButton(text=dct[lang_][22]), KeyboardButton(text=dct[lang_][23])]
    #     knbutton3 = [KeyboardButton(text=dct[lang_][31])]
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][17],
    #                              reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2,knbutton3],
    #                                                               resize_keyboard=True))
    # if stage_ == 12 and message in dct[lang_][18:24] or stage_ == 12 and message == dct[lang_][31]:
    #     cur.execute(upd_FILIAL.format(message, user_id))
    #     cur.execute(stagee.format('{}', user_id).format(13))
    #     connect.commit()
    #
    #     knbutton = [KeyboardButton(text=dct[lang_][25]), KeyboardButton(text=dct[lang_][26])]
    #     knbutton1 = [KeyboardButton(text=dct[lang_][27]), KeyboardButton(text=dct[lang_][28])]
    #     knbutton2 = [KeyboardButton(text=dct[lang_][29]), KeyboardButton(text=dct[lang_][30])]
    #     knbutton3 = [KeyboardButton(text=dct[lang_][31]), KeyboardButton(text=dctm[lang_ - 1])]
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][24],
    #                              reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1, knbutton2, knbutton3],
    #                                                               resize_keyboard=True))
    # elif stage_ == 12 and message not in dct[lang_][18:32]:
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][17])
    #     return
    #
    # if stage_ == 13 and message in dct[lang_][25:32] or stage_ == 13 and message == dct[lang_][
    #     41] or stage_ == 13 and message in dctm:
    #     cur.execute(upd_NEWJOB.format(message, user_id))
    #     cur.execute(stagee.format('{}', user_id).format(14))
    #     connect.commit()
    #
    #     knbutton = [KeyboardButton(text=dct[lang_][33]), KeyboardButton(text=dct[lang_][34])]
    #     knbutton1 = [KeyboardButton(text=dctt[lang_ - 1])]
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][32],
    #                              reply_markup=ReplyKeyboardMarkup([knbutton, knbutton1], resize_keyboard=True))
    # elif stage_ == 13 and message not in dct[lang_][25:32] or stage_ == 13 and message != dct[lang_][41] :
    #
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][24])
    # if stage_ == 14 and message in dctt:
    #     cur.execute(stagee.format('{}', user_id).format(555))
    #     connect.commit()
    #     context.bot.send_message(chat_id=user_id, text=dddq[lang_ - 1])
    #     pass
    # if stage_ == 14 and message in dct[lang_][33:35] or stage_==555 and message not in dddq:
    #     cur.execute(upd_WORKTIME.format(message, user_id))
    #     cur.execute(stagee.format('{}', user_id).format(15))
    #     connect.commit()
    #     knbutton = [KeyboardButton(text=dct[lang_][33]), KeyboardButton(text=dct[lang_][34])]
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][35],
    #                              reply_markup=ReplyKeyboardRemove([knbutton], resize_keyboard=True))
    # elif stage_ == 14 and message not in dct[lang_][33:35] and message not in dctt:
    #
    #     context.bot.send_message(chat_id=user_id, text=dct[lang_][32])
    # try:
    #     message = message.replace(' ', '')
    #     message = int(message)
    #     if stage_ == 15 and message not in dct[lang_][33:35] and len(str(message)) >= 7:
    #         cur.execute(upd_SALARY.format(str(message), user_id))
    #         cur.execute(stagee.format('{}', user_id).format(100))
    #         connect.commit()
    #         context.bot.send_message(chat_id=user_id, text=ddd[lang_ - 1])
    #     if stage_ == 15 and len(str(message)) < 7:
    #         context.bot.send_message(chat_id=user_id, text=dct[lang_][35])
    # except Exception:
    #     if stage_ == 15 and message not in dct[lang_][33:35]:
    #         context.bot.send_message(chat_id=user_id, text=dct[lang_][35])
    #

def xuzb(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(3)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Номзодлик анкетасини тўлдириш')
    context.bot.send_message(chat_id=user_id,
                             text='Фамилиянгиз, Исмингиз ва отангизни исмини қуйидаги кўринишда киритинг: \nРустамжонов Илхомжон Анвар ўғли')
def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Заполнения анкеты кандидата')
    context.bot.send_message(chat_id=user_id,
                             text='Заполнить ФИО в нижеследующем образце: \nРустамжанов Ильхом Анварович')
    sleep(1)

    connect.commit()
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='Nomzodlik anketasini  to’ldirish')
    context.bot.send_message(chat_id=user_id,
                             text='Familiyangiz, Ismingiz va otangizni ismini quyidagi korinishda kiriting: \nRustamjonov Ilhomjon Anvar o’g’li')
    sleep(1)
    connect.commit()
def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('b_users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()

    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][0], reply_markup=ReplyKeyboardRemove([k_but]))


def adm(update, context):
    user_id = update.message.chat_id
    text = update.message.caption




    try:
        photo_id = update.message.photo[-1].file_id
    except Exception:
        pass
    file = context.bot.getFile(photo_id)
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()

    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    bdate = cur.execute(select_BDATE.format(user_id)).fetchall()
    edu = cur.execute(select_EDU.format(user_id)).fetchall()
    edu_place = cur.execute(select_EDU_PLACE.format(user_id)).fetchall()
    last_job = cur.execute(select_LJOB.format(user_id)).fetchall()
    adress = cur.execute(select_DOM.format(user_id)).fetchall()
    l_dom = cur.execute(select_L_DOM.format(user_id)).fetchall()
    edulang = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    filial = cur.execute(select_FILIAL.format(user_id)).fetchall()
    njob = cur.execute(select_NEWJOB.format(user_id)).fetchall()
    wtime = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    salary = cur.execute(select_SALARY.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    Litsey = cur.execute(select_Litsey.format(user_id)).fetchall()
    inst = cur.execute(select_INST.format(user_id)).fetchall()
    tt = cur.execute(select_TT.format(user_id)).fetchall()
    oqi = cur.execute(select_OQI.format(user_id)).fetchall()
    qq = cur.execute(select_QQ.format(user_id)).fetchall()
    qq = cur.execute(select_QQ.format(user_id)).fetchall()
    bb = cur.execute(select_BB.format(user_id)).fetchall()
    connect.commit()

    try:

        Litsey = Litsey[0][0]
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        pnum_ = p_num[0][0]
        bdate = bdate[0][0]
        edu = edu[0][0]
        edu_place = edu_place[0][0]
        last_job = last_job[0][0]
        adress = adress[0][0]
        l_dom = l_dom[0][0]
        edulang = edulang[0][0]
        filial = filial[0][0]
        njob = njob[0][0]
        wtime = wtime[0][0]
        salary = salary[0][0]
        inst = inst[0][0]
        tt = tt[0][0]
        oqi = oqi[0][0]
        qq = qq[0][0]
        bb = bb[0][0]

    except Exception:
        pass
    anketa = ""
    if lang_ == 3:
        if a_name != ' ' and stage_ == 18:
            anketa = anketa + 'Исми:  {}\n<br>'.format(a_name)

        if pnum_ != ' ' and stage_ == 18:
            anketa = anketa + 'Телефон номер:  {}\n<br>'.format(pnum_)

        if bdate != ' ' and stage_ == 18:
            anketa = anketa + 'Тугилган санаси:  {}\n<br>'.format(bdate)

        if njob != ' ' and stage_ == 18:
                anketa = anketa + 'Малумоти:  {}\n<br>'.format(njob)

        if salary != ' ' and stage_ == 18:
            anketa = anketa + 'Битирилган лицей/колледж:  {}\n<br>'.format(salary)

        if qq != ' ' and stage_ == 18:
            anketa = anketa + 'Статус:  {}\n<br>'.format(qq)

        if tt != ' ' and stage_ == 18:
            anketa = anketa + 'Укилаётган О.Т.М:  {}\n<br>'.format(tt)


        if edu != ' ' and stage_ == 18:
            anketa = anketa + 'Битирилган ОТМ:  {}\n<br>'.format(edu)

        if Litsey != ' ' and stage_ == 18:
            anketa = anketa + 'Мутахассислигингиз диплом бўйича:  {}\n<br>'.format(Litsey)

        if edu_place != ' ' and stage_ == 18:
            anketa = anketa + 'Қўшимча сертификатингиз хақида маълумот:  {}\n<br>'.format(edu_place)

        if inst != ' ' and stage_ == 18:
            anketa = anketa + 'Иш тажрибаси:  {}\n<br>'.format(inst)

        if l_dom != ' ' and stage_ == 18:
            anketa = anketa + 'Кутилаетган лавозим:  {}\n<br>'.format(l_dom)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Иш жойи:  {}\n<br>'.format(edulang)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Тил:  {}\n<br>'.format(adress)


        if last_job != ' ' and stage_ == 18:
            anketa = anketa + 'Яшаш манзили:  {}\n'.format(last_job)

        if filial != ' ' and stage_ == 18:
            anketa = anketa + '<br>Кутилаётган ойлик маош:  {}\n'.format(str(filial))

    if lang_ == 1:
        if a_name != ' ' and stage_ == 18:
            anketa = anketa + 'Имя:  {}\n<br>'.format(a_name)

        if pnum_ != ' ' and stage_ == 18:
            anketa = anketa + 'Телефон номер:  {}\n<br>'.format(pnum_)

        if bdate != ' ' and stage_ == 18:
            anketa = anketa + 'Дата рождение:  {}\n<br>'.format(bdate)

        if njob != ' ' and stage_ == 18:
                anketa = anketa + 'Образование:  {}\n<br>'.format(njob)

        if salary != ' ' and stage_ == 18:
            anketa = anketa + 'Оконченный лицей/колледж:  {}\n<br>'.format(salary)

        if qq != ' ' and stage_ == 18:
            anketa = anketa + 'Статус:  {}  \n<br>'.format(qq)

        if tt != ' ' and stage_ == 18:
            anketa = anketa + '<br>Текущий ВУЗ:  {}\n<br>'.format(tt)



        if edu != ' ' and stage_ == 18:
            anketa = anketa + 'Оконченный ВУЗ:  {}\n<br>'.format(edu)

        if Litsey != ' ' and stage_ == 18:
            anketa = anketa + 'Спецификация по диплому:  {}\n<br>'.format(Litsey)

        if edu_place != ' ' and stage_ == 18:
            anketa = anketa + 'Сведение о дополнительном сертификате:  {}\n<br>'.format(edu_place)

        if inst != ' ' and stage_ == 18:
            anketa = anketa + 'Стаж работы:  {}\n<br>'.format(inst)

        if l_dom != ' ' and stage_ == 18:
            anketa = anketa + 'Ожидаемая должность:  {}\n<br>'.format(l_dom)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Место работы:  {}\n<br>'.format(edulang)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Язык:  {}\n<br>'.format(adress)


        if last_job != ' ' and stage_ == 18:
            anketa = anketa + 'Место жительство:  {}\n'.format(last_job)

        if filial != ' ' and stage_ == 18:
            anketa = anketa + '<br>Ожидаемая зарплата:  {}\n'.format(str(filial))

    if lang_ == 2:
        if a_name != ' ' and stage_ == 18:
            anketa = anketa + 'Ismi:  {}\n<br>'.format(a_name)

        if pnum_ != ' ' and stage_ == 18:
            anketa = anketa + 'Telefon raqami:  {}\n<br>'.format(pnum_)

        if bdate != ' ' and stage_ == 18:
            anketa = anketa + 'Tug`ilgan sanasi:  {}\n<br>'.format(bdate)

        if njob != ' ' and stage_ == 18:
                anketa = anketa + 'Ma`lumoti:  {}\n<br>'.format(njob)

        if salary != ' ' and stage_ == 18:
            anketa = anketa + 'Bitirilgan litsey/kolledj:  {}\n<br>'.format(salary)

        if qq != ' ' and stage_ == 18:
            anketa = anketa + 'Status:  {}\n<br>'.format(qq)

        if tt != ' ' and stage_ == 18:
            anketa = anketa + 'O`qilayotgan OTM:  {}\n<br>'.format(tt)


        if edu != ' ' and stage_ == 18:
            anketa = anketa + 'Bitirilgan OTM:  {}\n<br>'.format(edu)

        if Litsey != ' ' and stage_ == 18:
            anketa = anketa + 'Mutahassisligingiz diplom bo’yicha:  {}\n<br>'.format(Litsey)

        if edu_place != ' ' and stage_ == 18:
            anketa = anketa + 'Qo’shimcha sertifikatingiz haqida ma’lumot:  {}\n<br>'.format(edu_place)

        if inst != ' ' and stage_ == 18:
            anketa = anketa + 'Ish staji:  {}\n<br>'.format(inst)

        if l_dom != ' ' and stage_ == 18:
            anketa = anketa + 'Kutilayotgan lavozimi:  {}\n<br>'.format(l_dom)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Ish joyi:  {}\n<br>'.format(edulang)

        if edulang != ' ' and stage_ == 18:
            anketa = anketa + 'Til:  {}\n<br>'.format(adress)


        if last_job != ' ' and stage_ == 18:
            anketa = anketa + 'Yashash manzili:  {}\n'.format(last_job)

        if filial != ' ' and stage_ == 18:
            anketa = anketa + '<br>Kutilayotgan oylik maosh:  {}\n'.format(str(filial))


    # if stage_ == 16:
    #    user_name = update.message.from_user.username
    #    file = context.bot.getFile(photo_id)
    #    file.download('Picture.jpeg')
    #    context.bot.send_photo(photo=open('{}.pdc'.format(user_id), 'rb'), chat_id=-772939946)
    #    context.bot.send_photo(photo=open('{}.jpeg'.format(user_id+1), 'rb'), chat_id=-772939946)
    #    context.bot.send_photo(photo=open('{}.jpeg'.format(user_id + 2), 'rb'), chat_id=-772939946)
    #    context.bot.send_photo(photo=open('{}.jpeg'.format(user_id + 3), 'rb'), chat_id=-772939946, caption=anketa , parse_mode='Markdown')
    #    context.bot.send_message(chat_id=-772939946, text='@'+user_name)
    #    context.bot.send_message(chat_id=user_id, text=dct[lang_][37])
    #    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    #    connect.commit()
    #    import os
    #    if os.path.isfile('Picture.jpeg'.format(user_id)):
    #        os.remove('Picture.jpeg'.format(user_id))
    #        print("success")
    #    else:
    #        print("File doesn't exists!")
    #    if os.path.isfile('{}.jpeg'.format(user_id)):
    #        os.remove('{}.jpeg'.format(user_id))
    #        print("success")
    #    else:
    #        print("File doesn't exists!")
    #    if os.path.isfile('{}.jpeg'.format(user_id+1)):
    #        os.remove('{}.jpeg'.format(user_id+1))
    #        print("success")
    #    else:
    #        print("File doesn't exists!")

    if stage_ == 18:
        cur.execute(stagee.format('{}', user_id).format(19))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][37])
        file.download('{}.jpeg'.format(user_id+3))

        telegraph.create_account(short_name='1333')
        print(anketa)
        with open(f'''{user_id+3}.jpeg''', 'rb') as f:
            path = requests.post('https://telegra.ph/upload', files={'file': ('file', f, 'image/jpеg')}).json()[0]['src']

        html = f'''
        <p>{l_dom}</p>
        <img src={path}/>
        <p>{anketa}</p>


        '''

        response = telegraph.create_page(
            '{}'.format(a_name),
            html_content=html)

        context.bot.send_message(chat_id=-688428587, text=f'''http://telegra.ph/{response['path']}''')

    # if lang_ == 1 and stage_ == 16 and edu_place != ' ' and last_job != ' ':
    #     anketa = """
    # Имя:  {}
    # Телефон номер:  {}
    # Дата рождения:  {}
    # Статус:  {}
    # Образование:  {}
    # Законченное В.У.З:  {}
    # Место работы:  {}
    # Адрес:  {}
    # Владеющиеся языки:  {}
    # Филиал:  {}
    # Желаемая должность:  {}
    # Смена:  {}
    # Желаемая зарплата:  {}
    #         """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, last_job, adress, edulang, filial, njob, wtime,
    #                    salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 2 and stage_ == 16 and edu_place != ' ' and last_job != ' ':
    #     anketa = """
    #         Ismi:  {}
    #         Telefon:  {}
    #         Tugilgan sanasi:  {}
    #         Status:  {}
    #         Malumoti:  {}
    #         Bitrgan O.T.M.:  {}
    #         Ish joyi:  {}
    #         Manzili:  {}
    #         Til:  {}
    #         Filial:  {}
    #         Istalayotgan ish lavozimi:  {}
    #         Smena:  {}
    #         Istalayotgan oylik maoshi:  {}
    #                 """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, last_job, adress, edulang, filial, njob,
    #                            wtime,
    #                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 3 and stage_ == 16 and edu_place != ' ' and last_job != ' ':
    #     anketa = """
    #         Исми:  {}
    #         Телефон :  {}
    #         Тугилган санаси:  {}
    #         Статус:  {}
    #         Малумоти:  {}
    #         Битирган О.Т.М.:  {}
    #         Иш жойи:  {}
    #         Манзил:  {}
    #         Тил:  {}
    #         Филиал:  {}
    #         Исталайотган иш лавозими :  {}
    #         Смена:  {}
    #         Исталайотган ойлик маош:  {}
    #                 """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, last_job, adress, edulang, filial, njob,
    #                            wtime,
    #                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    #
    # if lang_ == 1 and stage_ == 16 and edu_place == ' ':
    #     anketa = """
    #                 Имя:  {}
    #                 Телефон номер:  {}
    #                 Дата рождения:  {}
    #                 Статус:  {}
    #                 Образование:  {}
    #                 Место работы:  {}
    #                 Адрес:  {}
    #                 Владеющиеся языки:  {}
    #                 Филиал:  {}
    #                 Желаемая должность:  {}
    #                 Смена:  {}
    #                 Желаемая зарплата:  {}
    #                         """.format(a_name, pnum_, bdate, l_dom, edu, last_job, adress, edulang, filial, njob, wtime,
    #                                    salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 2 and stage_ == 16 and edu_place == ' ':
    #     anketa = """
    #                         Ismi:  {}
    #                         Telefon:  {}
    #                         Tugilgan sanasi:  {}
    #                         Status:  {}
    #                         Malumoti:  {}
    #                         Ish joyi:  {}
    #                         Manzili:  {}
    #                         Til:  {}
    #                         Filial:  {}
    #                         Istalayotgan ish lavozimi:  {}
    #                         Smena:  {}
    #                         Istalayotgan oylik maoshi:  {}
    #                                 """.format(a_name, pnum_, bdate, l_dom, edu, last_job, adress, edulang, filial,
    #                                            njob,
    #                                            wtime,
    #                                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 3 and stage_ == 16 and edu_place == ' ':
    #     anketa = """
    #                         Исми:  {}
    #                         Телефон :  {}
    #                         Тугилган санаси:  {}
    #                         Статус:  {}
    #                         Малумоти:  {}
    #                         Битирган О.Т.М.:  {}
    #                         Иш жойи:  {}
    #                         Манзил:  {}
    #                         Тил:  {}
    #                         Филиал:  {}
    #                         Исталайотган иш лавозими :  {}
    #                         Смена:  {}
    #                         Исталайотган ойлик маош:  {}
    #                                 """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, last_job, adress, edulang,
    #                                            filial, njob,
    #                                            wtime,
    #                                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    #
    # if lang_ == 1 and stage_ == 16 and last_job == ' ':
    #     anketa = """
    #                 Имя:  {}
    #                 Телефон номер:  {}
    #                 Дата рождения:  {}
    #                 Статус:  {}
    #                 Образование:  {}
    #                 Законченное В.У.З:  {}
    #                 Адрес:  {}
    #                 Владеющиеся языки:  {}
    #                 Филиал:  {}
    #                 Желаемая должность:  {}
    #                 Смена:  {}
    #                 Желаемая зарплата:  {}
    #                         """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, adress, edulang, filial, njob,
    #                                    wtime,
    #                                    salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 2 and stage_ == 16 and last_job == ' ':
    #     anketa = """
    #                         Ismi:  {}
    #                         Telefon:  {}
    #                         Tugilgan sanasi:  {}
    #                         Status:  {}
    #                         Malumoti:  {}
    #                         Bitrgan O.T.M.:  {}
    #                         Manzili:  {}
    #                         Til:  {}
    #                         Filial:  {}
    #                         Istalayotgan ish lavozimi:  {}
    #                         Smena:  {}
    #                         Istalayotgan oylik maoshi:  {}
    #                                 """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, adress, edulang,
    #                                            filial, njob,
    #                                            wtime,
    #                                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()
    # if lang_ == 3 and stage_ == 16 and last_job == ' ':
    #     anketa = """
    #                         Исми:  {}
    #                         Телефон :  {}
    #                         Тугилган санаси:  {}
    #                         Статус:  {}
    #                         Малумоти:  {}
    #                         Битирган О.Т.М.:  {}
    #                         Манзил:  {}
    #                         Тил:  {}
    #                         Филиал:  {}
    #                         Исталайотган иш лавозими :  {}
    #                         Смена:  {}
    #                         Исталайотган ойлик маош:  {}
    #                                 """.format(a_name, pnum_, bdate, l_dom, edu, edu_place, adress, edulang,
    #                                            filial, njob,
    #                                            wtime,
    #                                            salary)
    #     context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=user_id, caption=anketa)
    #     cur.execute(stagee.format('{}', user_id).format(17))
    #     connect.commit()