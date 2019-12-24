from telegram.ext import Updater, CommandHandler
import pokepy
from modules import Type

START_TEXT = 'Hey! Pokedex here. Type /help to get list of commands'

poke_client = pokepy.V2Client(cache='in_disk', cache_location='/home/abhayk/.cache')

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def start(update, context):
    update.message.reply_text(text = START_TEXT)

def get_help(update, context):
    update.message.reply_text("""
List of available commands:
/hello
/help
/type - Get a Pokemon's type(s) and type weaknesses
      """)

def get_type(update, context):
	if len(context.args) == 1:
		response = ''
		response = Type.fetch_type(poke_client, context.args[0])
		update.message.reply_text(response)
	else:
		update.message.reply_text("Usage: /type Pikachu")



updater = Updater(open('API_TOKEN','r').read().replace('\n',''), use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', get_help))
updater.dispatcher.add_handler(CommandHandler('type', get_type))

updater.start_polling()
updater.idle()
