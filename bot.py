import os
from telegram.ext import Updater, CommandHandler
import pokepy
from modules import Type, Pic, Ability, Learnset, Random, Starter, AllInfo
import logging
START_TEXT = 'Hey! Pokedex here. Type /help to get list of commands'
ABOUT_TEXT = 'Bot made by Abhay Kshatriya (vegeto1806 on Telegram).\nThe source is available at https://github.com/kshatriya-abhay/pokebot'
HELP_TEXT = """
List of available commands:
/help - Get this list
/about - About the bot
Modules:
/pokedex - Gets the ability, type and learnset of a Pokemon
/ability - Get info about an ability/a Pokemon's all abilities
/learnset - Get Bulbapedia link to Learnset of a Pokemon
/pic - Get a Pokemon's sprite
/random - Get a random pokemon
/type - Get a Pokemon's type(s) and type weaknesses
/starter - Gets you your own unique starter pokemon
"""

poke_client = pokepy.V2Client(cache='in_disk', cache_location=(os.environ['HOME']+'/.cache'))

def parse_args(args):
	return '-'.join(args).lower()

def start(update, context):
    update.message.reply_text(text = START_TEXT)

def about(update, context):
    update.message.reply_text(text = ABOUT_TEXT)

def get_help(update, context):
    update.message.reply_text(HELP_TEXT)

def all_info(update, context):
	if len(context.args) >= 1:
		query = parse_args(context.args)
		response = ''
		response = AllInfo.get_all_info(poke_client, query)
		update.message.reply_text(response, parse_mode = 'Markdown')
	else:
		update.message.reply_text("Usage: /pokedex Pikachu")

def get_type(update, context):
	if len(context.args) >= 1:
		query = parse_args(context.args)
		response = ''
		response = Type.fetch_type(poke_client, query)
		update.message.reply_text(response)
	else:
		update.message.reply_text("Usage: /type Pikachu")

def get_pic(update, context):
	if len(context.args) >= 1:
		query = parse_args(context.args)
		flag, response, pic_title = Pic.fetch_pic(poke_client, query)
		if flag:
			context.bot.send_photo(chat_id=update.effective_chat.id, photo=response, caption=pic_title, reply_to_message_id=update.effective_message.message_id)
			pass
		else:
			update.message.reply_text(response)
	else:
		update.message.reply_text("Usage: /pic Pikachu")

def ability(update, context):
	if len(context.args) >= 1:
		query = parse_args(context.args)
		response = Ability.get_ability(poke_client, query)
		update.message.reply_text(response, parse_mode = 'Markdown')
	else:
		update.message.reply_text("Usage: /ability Pikachu")

def learnset(update, context):
	if len(context.args) >= 1:
		query = parse_args(context.args)
		response = Learnset.get_learnset(poke_client, query)
		update.message.reply_text(response, parse_mode = 'Markdown')
	else:
		update.message.reply_text("Usage: /learnset Pikachu")

def get_random(update, context):
	response = Random.get_random_pokemon(poke_client)
	update.message.reply_text(response, parse_mode = 'Markdown')

def starter(update, context):
	response = Starter.get_starter_pokemon(poke_client, update.message.from_user.id)
	update.message.reply_text(response, parse_mode = 'Markdown')


if __name__ == "__main__":

	#TOKEN = open('API_TOKEN','r').read().replace('\n','')
	TOKEN = os.environ.get('API_TOKEN')

	NAME = "veg-pokebot"

    # Port is given by Heroku
	PORT = os.environ.get('PORT')

	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

	updater = Updater(TOKEN, use_context=True)

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('about', about))
	updater.dispatcher.add_handler(CommandHandler('help', get_help))
	updater.dispatcher.add_handler(CommandHandler('pokedex', all_info))
	updater.dispatcher.add_handler(CommandHandler('type', get_type))
	updater.dispatcher.add_handler(CommandHandler('pic', get_pic))
	updater.dispatcher.add_handler(CommandHandler('ability', ability))
	updater.dispatcher.add_handler(CommandHandler('learnset', learnset))
	updater.dispatcher.add_handler(CommandHandler('random', get_random))
	updater.dispatcher.add_handler(CommandHandler('starter', starter))

	# Start the webhook

	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
	updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))

	#updater.start_polling()
	updater.idle()
