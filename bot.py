import telebot
import pyowm
from pyowm.utils.config import get_default_config
import os


config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = pyowm.OWM('2b876c6a4673d7e93333d478439e43d5', config_dict)


@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	m = w.detailed_status
	temp = w.temperature('celsius')["temp"]
	temp = round(temp)

	answer = 'В вашем городе ' + message.text +' сейчас '+ m + '\n'
	answer += 'Темпиратура примерно ' + str(temp) + ' °C' + '\n\n'

	bot.send_message(message.chat.id, answer )

token = os.environ.get('BOT_TOKEN')

bot.polling( none_stop = True )