import pokepy

def fetch_pic(api,pkm):
	try:
		pika = api.get_pokemon(pkm)
	except:
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
	
	IMG_URL = pika.sprites.front_default

	print(IMG_URL) # logging

	response = IMG_URL
	return True, response, pika.name.capitalize()


