def get_learnset(api, query):
    try:
        pikasp = api.get_pokemon_species(query)
    except:
        response = "Seems like that ain't a valid Pokemon name.."
        return response
    gen_name = pikasp.generation.name
    str_list = gen_name.split('-')
    str_list[0] = str_list[0].title()  # Generation
    str_list[1] = str_list[1].upper()  # IV etc

    PRE_URL = 'https://bulbapedia.bulbagarden.net/wiki/'
    pname = ''
    for n in pikasp.names:
        if n.language.name == 'en':
            pname = n.name
    MID = pname + '_%28Pokémon%29/'
    END = str_list[0] + '_' + str_list[1] + '_learnset'
    B_URL = PRE_URL + MID + END
    response = '[Gen '+ str_list[1] +' learnset](' + B_URL + ')' + '\n'

    if pikasp.generation.name != 'generation-vii' and pikasp.generation.name != 'generation-viii':
        END = str_list[0] + '_VII_learnset'
        B_URL = PRE_URL + MID + END
        response = response + '[Gen VII learnset](' + B_URL + ')'
    return response
