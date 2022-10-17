import telebot
import random

TOKEN = 'ваш токен'
bot = telebot.TeleBot(TOKEN)
answers = ['Так', 'Ні', 'Не можу відповісти...', 'Запитай пізніше', 'Без сумніву', 'Ніколи в житті', 'На жаль, ні', 'Все в твоїх руках', 'Звичайно', 'Мені потрібний відпочинок, запитай пізніше', 'Однозначно так', 'Хороші перспективи', 'Краще не розповідати', 'Дуже сумнівно', 'Перспективи не дуже хороші', 'Навіть не думай', 'Зараз не можна передбачити']


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привіт, напиши запитання, яке тебе цікавить:)')


@bot.message_handler(commands=["help"])
def about(m, res=False):
    bot.send_message(m.chat.id, 'Це магічна куля, яка розроблена для передбачення майбутнього.')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, random.choice(answers))


bot.polling(none_stop=True, interval=0)
