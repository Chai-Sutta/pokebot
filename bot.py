import os
from telegram.ext import Updater, CommandHandler
import pokepy
from modules import Type

START_TEXT = 'Hey! Pokedex here. Type /help to get list of commands'
ABOUT_TEXT = 'Bot made by Abhay Kshatriya (vegeto1806 on Telegram).\nThe source is available at https://github.com/kshatriya-abhay/pokebot'
HELP_TEXT = """
List of available commands:
/help
/about - About the bot
/type - Get a Pokemon's type(s) and type weaknesses
"""

poke_client = pokepy.V2Client(cache='in_disk', cache_location=(os.environ['HOME']+'/.cache'))

def start(update, context):
    update.message.reply_text(text = START_TEXT)

def about(update, context):
    update.message.reply_text(text = ABOUT_TEXT)

def get_help(update, context):
    update.message.reply_text(HELP_TEXT)

def get_type(update, context):
	if len(context.args) == 1:
		response = ''
		response = Type.fetch_type(poke_client, context.args[0])
		update.message.reply_text(response)
	else:
		update.message.reply_text("Usage: /type Pikachu")


TOKEN_STRING = open('API_TOKEN','r').read().replace('\n','')
updater = Updater(TOKEN_STRING, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('about', about))
updater.dispatcher.add_handler(CommandHandler('help', get_help))
updater.dispatcher.add_handler(CommandHandler('type', get_type))

updater.start_polling()
updater.idle()
