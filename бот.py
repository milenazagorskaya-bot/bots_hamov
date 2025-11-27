

import telebot
from config import API_TOKEN
from telebot.tipes import (ReplyKeyboardMarkup, ReplyKeybordMarkup, ReplyKeyboardRemove, Message)

keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text='налево')
button2 = KeyboardButton(text='направо')

keyboard.add(button)
keyboard.add(button2)

API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)

state = 0

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    hello_message = f'ПРивет! <b>{message.from_user.username}<b>!'
    bot.send_message(
        message.chat.id,
        hello_message,
        reply_markup=keyboard,
        parse_mode='HTML'
        )
    state = 1
 


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def text_message(message: Message:
                 global state
                 if state == 1 and message.text == "налево":
                 bot.send_message(
                     message.chat.id,
                     'вы пошли налево'
                     )
                 state = 2
            elif  state == 1 and message.text == "направо":
                 bot.send_message(
                     message.chat.id,
                     'вы пошли направо'
                     )
                 state = 3
            else:
                bot.send_message(
                     message.chat.id,
                     'вы нажали что-то не то'
                
                 
