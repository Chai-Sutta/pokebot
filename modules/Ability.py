import pokepy

def get_ability_text(api, ability_text, is_hidden = False):
	ability = api.get_ability(ability_text)
	flavor = ''
	flavor = ability.name.title().replace('-',' ')
	if is_hidden:
		flavor = flavor + ' (Hidden Ability)'
	flavor = flavor + '\n'
	for fte in ability.flavor_text_entries:
		if fte.language.name == 'en':
			flavor = flavor + fte.flavor_text + '\n'
			break
	url_text = ability_text.title().replace('-','_')
	B_URL = 'https://bulbapedia.bulbagarden.net/wiki/' + url_text + '_%28Ability%29'
	flavor = flavor + '[Bulbapedia page]('+B_URL+')' + '\n'
	flavor = flavor + '\n'
	return flavor

def get_ability(api, query):
	response = ''
	try:
		pok = api.get_pokemon(query)
		response = 'List of abilities for ' + pok.name.title().replace('-',' ') + '\n'
		response = response + '\n'
		for a in pok.abilities:
			response = response + get_ability_text(api, a.ability.name, a.is_hidden)
	except:
		try:
			response = get_ability_text(api, query)
		except:
			response = 'Invalid query'
	return response