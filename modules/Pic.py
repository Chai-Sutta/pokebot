import pokepy

def fetch_pic(api,pkm):
	try:
		pikasp = api.get_pokemon_species(pkm)
	except:
		ans = "Seems like that ain't a valid Pokemon name.."
		return False, ans, ''
	pid = pikasp.id
	pika = api.get_pokemon(pid)

	# PRE_URL = 'https://pokeres.bastionbot.org/images/pokemon/'
	# EXT = '.png'
	# IMG_URL = PRE_URL+str(pid)+EXT
	
	IMG_URL = pika.sprites.front_default

	print(IMG_URL) # logging is for kids, real men print()

	response = IMG_URL
	return True, response, pika.name.capitalize()


