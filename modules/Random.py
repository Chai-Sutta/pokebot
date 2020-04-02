import pokepy
import random

def get_random_pokemon(api):
	query = random.randint(1,807)
	response = ''
	try:
		pikasp = api.get_pokemon_species(query)
	except:
		response = "What? This shouldn't happen..."
		return response

	PRE_URL = 'https://bulbapedia.bulbagarden.net/wiki/'
	pname = ''
	for n in pikasp.names:
		if n.language.name == 'en':
			pname = n.name
	MID = pname + '_%28Pokémon%29'
	B_URL = PRE_URL+MID
	print(B_URL)
	response = 'Your random pokémon is: '+pname+'\n'+'[Bulbapedia page]('+B_URL+')'
	return response