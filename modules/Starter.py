def get_starter_pokemon(api, user_id):
    query = (user_id % 807) + 1
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
    B_URL = PRE_URL + MID
    response = 'Your unique starter pokémon is: [' + pname + '](' + B_URL + ')'
    return response
