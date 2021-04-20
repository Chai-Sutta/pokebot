import pokepy
from bs4 import BeautifulSoup
import requests

def fetch_pic(api,pkm):
	try:
		pikasp = api.get_pokemon_species(pkm)
		pid = pikasp.id
		pika = api.get_pokemon(pid)
	except:
		ans = "Seems like that ain't a valid Pokemon name.."
		return False, ans, ''

	# PRE_URL = 'https://pokeres.bastionbot.org/images/pokemon/'
	# EXT = '.png'
	# IMG_URL = PRE_URL+str(pid)+EXT

	# IMG_URL = pika.sprites.front_default

	for n in pikasp.names:
		if n.language.name == 'en':
			pname = n.name
	B_URL = 'https://bulbapedia.bulbagarden.net/wiki/' + pname + '_%28Pokémon%29'
	bulba_page = requests.get(B_URL)
	root = BeautifulSoup(bulba_page.content, "html5lib")
	IMG_URL = root.find(property="og:image").get('content')

	print(IMG_URL) # logging

	response = IMG_URL
	return True, response, pika.name.capitalize()


