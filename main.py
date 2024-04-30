import telebot
from telebot import types
import random
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot("7147534018:AAExmYMCMNvDSCoSeEF6SeFi8W9FjuywDa0")
cnt = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Что ты умеешь?')
        btn2 = types.KeyboardButton('Хочу завра!')
        btn3 = types.KeyboardButton('Расскажи о медитации.')
        btn4 = types.KeyboardButton('Расскажи о йоге!')
        btn5 = types.KeyboardButton('Включи музыку.')
        btn6 = types.KeyboardButton('Время йоги!')
        btn7 = types.KeyboardButton('Расскажи о психосоматике.')
        btn8 = types.KeyboardButton('Хочу цитату!')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)

    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.from_user.id, 'Я могу: \n • предложить Вам тест на примерный уровень вашей усталости;'
                                               ' \n • расссказать о средствах медитации; '
                                               '\n • посоветовать различные медитации; \n • прислать позитивные цитаты; '
                                               '\n • вывести список психосоматических терминов;'
                                               '\n • включить расслабляющую музыку')


    elif message.text == 'Расскажи о медитации.':
        media_group = []
        text = "Медита́ция (лат. meditatio — «размышление») — ряд психических упражнений," \
               " используемых в составе духовно-религиозной или оздоровительной практики," \
               " или же особое психическое состояние, возникающее в результате этих упражнений " \
               "(или в силу иных причин). Медитация может рассматриваться как вид созерцания (лат. contemplatio)." \
               "Занимаясь медитацией, согласно ряду традиций, не надо делать над собой никаких усилий, " \
               "нужно полностью расслабиться. Медитация — это состояние расслабленной сосредоточенности," \
               " в котором идет отрешённое наблюдение за происходящим." \
               "Медитация означает, что мы чему-то предоставляем место, позволяем этому развиваться," \
               " наблюдаем, воспринимаем во всей полноте. Занимающийся медитацией ничего не должен оценивать," \
               " предоставив свободу мыслям, чувствам и протекающим в организме процессам."

        for num in range(2):
            media_group.append(InputMediaPhoto(open(f'photo/meditation/{num + 1}.jpg', 'rb'),
                                               caption=text if num == 0 else ''))
        bot.send_media_group(chat_id=message.from_user.id, media=media_group)

    elif message.text == 'Включи музыку.':
        x = random.randint(1, 2)
        if x == 1:
            bot.send_message(message.from_user.id, 'Тибетские чаши – это средство медитации,'
                                                   ' которое издавна использовалось в духовной практике. Такие чаши изготавливаются '
                                                   'из уникального сплава металлов, который позволяет получить необычный звук, который'
                                                   ' существенно отличается от звучания любых других музыкальных инструментов. '
                                                   'Так же эти чаши часто называют поющими!')
            bot.send_audio(chat_id=message.from_user.id, audio=open("music/music_1.mp3", 'rb'))

        elif x == 2:
            bot.send_message(message.from_user.id, 'Звук дождя всегда успокаивает душу и очищает сознание.'
                                                   ' Под эти звуки сладко спится и легко думается.'
                                                   ' Под эти звуки приятно немного абстрагироваться от ситуации... \n'
                                                   'Может это то, что сейчас так необходимо?')
            bot.send_audio(chat_id=message.from_user.id, audio=open("music/music_2.mp3", 'rb'))

    elif message.text == 'Расскажи о йоге!':
        media_group = []
        text = 'Йо́га (дев. योग, IAST: yoga) — понятие в индийской культуре, в широком смысле означающее ' \
               'совокупность различных духовных, психических и физических практик, разрабатываемых в разных направлениях' \
               ' индуизма и буддизма и нацеленных на управление психическими и физиологическими функциями организма' \
               ' с целью достижения индивидуумом возвышенного духовного и психического состояния. \n' \
               'В более узком смысле, йога — одна из шести ортодоксальных школ (даршан) философии индуизма.'
        media_group.append(InputMediaPhoto(open(f'photo/uoga/osn.jpg', 'rb'),
                                           caption=text))
        bot.send_media_group(chat_id=message.from_user.id, media=media_group)

    elif message.text == 'Время йоги!':
        media_group = []
        text = 'Попробуйте данные позы для медитации. \n Перед упражнениями прочитайте подробнее о психосоматике и медитации'
        for num in range(3):
            media_group.append(InputMediaPhoto(open(f'photo/uoga/{num + 1}.jpg', 'rb'),
                                               caption=text if num == 0 else ''))
        bot.send_media_group(chat_id=message.from_user.id, media=media_group)

    elif message.text == 'Расскажи о психосоматике.':
        bot.send_message(message.from_user.id, 'Начнём! \n'
                                               'Психосоматика – междисциплинарное научное направление, в котором изучаются психологические, '
                                               'социальные и культурные факторы возникно вения телесных заболеваний. '
                                               'В этом направлении изучается влияние раздражающих факторов внешней среды на психологическое '
                                               'и телесное здоровье человека. \n'
                                               'Подробнее про это направление советую почитать в ' +
                         '[статье](https://clck.ru/Y6rKD)', parse_mode='Markdown')

    elif message.text == 'Хочу завра!':
        media_group = []
        text = 'Твой завр сегодня это....'
        x = random.randint(1, 15)
        media_group.append(InputMediaPhoto(open(f'photo/mudozavr/{x}.jpg', 'rb'),
                                           caption=text))
        bot.send_media_group(chat_id=message.from_user.id, media=media_group)

    elif message.text == 'Хочу цитату!':
        media_group = []
        x = random.randint(1, 8)
        text = random.choice(open('positiv.txt', 'r', encoding="utf-8").read().splitlines())
        print(text)
        media_group.append(InputMediaPhoto(open(f'photo/positive/{x}.jpg', 'rb'),
                                           caption=text))
        bot.send_media_group(chat_id=message.from_user.id, media=media_group)


bot.polling(none_stop=True, interval=0)