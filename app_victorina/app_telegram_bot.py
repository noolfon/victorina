"""
Use this token to access the HTTP API:
1591509567:AAE0JWurj9n_1lb9OCx_P53kjuMNauuJf_s
Keep your token secure and store it safely, it can be used by anyone to control your bot.

name fot telegram: @quiz_for_children_bot
"""
import telebot
from telebot import types
import models
import random

TOKEN = '1591509567:AAE0JWurj9n_1lb9OCx_P53kjuMNauuJf_s'

def random_riddels():
    random_num = random.randrange(1, 5115)
    for s in models.Riddles.select():
        if s.id == random_num:
            return [s.riddles, s.response]



bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def first(message):
    message_for_user = f"""Отгадай загадку:\n{random_riddels()[0]}"""

    key = types.ReplyKeyboardMarkup(True, False)
    bot.send_message(message.chat.id, message_for_user, reply_markup=key)


bot.polling()
