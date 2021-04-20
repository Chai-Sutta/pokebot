def get_evolution(api, query):
    try:
        pikasp = api.get_pokemon_species(query)
    except:
        response = "Seems like that ain't a valid Pokemon name.."
        return response
    response = ""
    chain_id = pikasp.evolution_chain.url.split('/')[-2]
    evo_chain = api.get_evolution_chain(chain_id)
    queue = [evo_chain.chain]
    while len(queue) != 0:
        current_chain = queue.pop(0)
        response = response + get_pokemon_name(api, current_chain.species) + '\n'
        try:
            next_list = current_chain.evolves_to
            for item in next_list:
                queue.append(item)
        except AttributeError:
            continue
    return response


def get_pokemon_name(api, species):
    species_id = species.url.split('/')[-2]
    sp = api.get_pokemon_species(species_id)
    pname = ''
    for n in sp.names:
        if n.language.name == 'en':
            pname = n.name
    return pname