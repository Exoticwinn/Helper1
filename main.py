import telebot
import time
from config import TOKEN
from logic import gen_pass, gen_emodji, flip_coin,get_random_fact,count_down

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.send_message(message.chat.id, gen_pass(8))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    bot.send_message(message.chat.id, gen_emodji())

@bot.message_handler(commands=['coin'])
def send_coin(message):
    bot.send_message(message.chat.id, flip_coin())

@bot.message_handler(commands=['fact'])
def send_fact(message):
    bot.send_message(message.chat.id, get_random_fact())

@bot.message_handler(commands=['countdown'])
def do_countdown(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.send_message(message.chat.id, "Укажите число после команды. Пример: /countdown 5")
        return

    try:
        number = int(parts[1])
        if number < 0:
            bot.send_message(message.chat.id, "Число должно быть неотрицательным.")
            return
        if number > 30:
            bot.send_message(message.chat.id, "Число не должно превышать 30.")
            return

        for i in range(number, -1, -1):
            bot.send_message(message.chat.id, str(i))
            time.sleep(1)

    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, укажите целое число. Пример: /countdown 10")

    number = int(parts[1])
    bot.send_message(message.chat.id, count_down(number))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
