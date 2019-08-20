import telebot
import random
import split

# Token
bot = telebot.TeleBot("759825642:AAERC44zGNqB9n3czBgQOtXHpOjcA3xElGI")
a = ["Подтверждаю", "Угу"]
b = 'подтверди'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Царь позвал к себе Иванушку-дурака и говорит:\n"
'– Если завтра не принесешь двух говорящих птиц – голову срублю.\n' 
'Иван принес филина и воробья. Царь говорит:\n'
'– Ну, пусть что-нибудь скажут.\n'
'Иван спрашивает:\n'
'– Воробей, почем раньше водка в магазине была?\n'
'Воробей:\n'
'– Чирик.\n'
'Иван филину:\n'
'– А ты, филин, подтверди.\n'
'Филин:\n'
'– Подтверждаю.')




@bot.message_handler(regexp="подтверди")
def answer(message):
    bot.send_message(message.from_user.id, random.choice(a))

@bot.message_handler(func=lambda m: True)
def answer(message):
     bot.send_message(message.from_user.id, 'ygy')

bot.polling(none_stop=True, interval=0)