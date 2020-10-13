import telebot
from flask import Flask, request
import os

TOKEN = "1378863044:AAH-DSNag60twwWlzpY-0uBy8BnxCWGcOEo"
bot = telebot.TeleBot
server = Flask(__name__)

def findat(msg):
	for i in msg:
		if '@' in i:
			return i


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '(placeholder text)')


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)

def at_converter(message):
	texts = message.text.split()
	at_text = findat(texts)
	if at_text == '@':
		pass
	else:
		insta_link="https://instagram.com/{}".format(at_text[1:])
		bot.reply_to(message, insta_link)

@server.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url='https://quiet-lowlands-57399.herokuapp.com/' + TOKEN)
	return "!", 200

if __name__ = "__main__":
	server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
	
