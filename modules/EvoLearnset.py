from .Evolution import get_evolution
from .Learnset import get_learnset


def get_evo_learnset(api, query):
    try:
        api.get_pokemon_species(query)
    except:
        response = "Seems like that ain't a valid Pokemon name.."
        return response
    response = ''
    evo_list = get_evolution(api, query).split('\n')[:-1]
    for pokemon in evo_list:
        response = response + pokemon + '\n' + get_learnset(api, pokemon) + '\n\n'
    return response
