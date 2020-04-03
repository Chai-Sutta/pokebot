
 
# -*- coding: future_fstrings -*-

#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
import pokepy
import random

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(PokedexMod())


@loader.tds
class PokedexMod(loader.Module):
    """Mini Pokedex"""
    strings = {"name": "Pokedex"
               }
    def config_complete(self):
        self.name = self.strings["name"]

    def parse_args(self, args):
        return '-'.join(args.split()).lower()

    def get_info(self, api, query):
        try:
            pikasp = api.get_pokemon_species(query)
        except:
            response = "Seems like that ain't a valid Pokemon name.."
            return response
        PRE_URL = 'https://bulbapedia.bulbagarden.net/wiki/'
        pname = ''
        for n in pikasp.names:
            if n.language.name == 'en':
                pname = n.name
        MID = pname + '_%28Pokémon%29'
        NAME_URL = PRE_URL+MID

        response = 'Pokemon : <a href="'+NAME_URL+'">' + pname + '</a>\n\n' + self.fetch_type(api, pikasp) + '\n' + self.get_ability(api, query)
        return response

    def fetch_type(self, api, pikasp):
        ans = ''
        pid = pikasp.id
        pika = api.get_pokemon(pid)
        
        ptypeList = pika.types
        typeList = []
        for t in ptypeList:
            typeList.append(api.get_type(t.type.name))
        dmg0 = []
        dmgh = []
        dmg2 = []
        for t in typeList:
            ans = ans + 'Type : ' + t.name.capitalize() + '\n'
            s1list = []
            s2list = []
            s3list = []
            for tn in t.damage_relations.no_damage_from:
                s1list.append(tn.name)
            for tn in t.damage_relations.half_damage_from:
                s2list.append(tn.name)
            for tn in t.damage_relations.double_damage_from:
                s3list.append(tn.name)
            dmg0.append(s1list)
            dmgh.append(s2list)
            dmg2.append(s3list)
        d0 = {}
        d25 = {}
        d50 = {}
        d200 = {}
        d400 = {}
        if len(typeList) > 1:
            d0 = set(dmg0[0]) | set(dmg0[1])
            d25 = set(dmgh[0]) & set(dmgh[1])
            d400 = set(dmg2[0]) & set(dmg2[1])
            d50 = ((set(dmgh[0]) - set(dmg2[1])) | (set(dmgh[1]) - set(dmg2[0]))) - d0 - d25 - d400
            d200 = ((set(dmg2[0]) - set(dmgh[1])) ^ (set(dmg2[1]) - set(dmgh[0]))) - d0 - d25 - d400
        else:
            d0 = set(dmg0[0])
            d50 = set(dmgh[0])
            d200 = set(dmg2[0])

        if d0:
            st = ''
            for t in d0:
                st = st + (t.capitalize()+', ')
            st = st[:-2]
            ans = ans + 'No Damage from ' + st + '\n'
        if d25:
            st = ''
            for t in d25:
                st = st + (t.capitalize()+', ')
            st = st[:-2]
            ans = ans + '1/4th Damage from ' + st + '\n'
        if d50:
            st = ''
            for t in d50:
                st = st + (t.capitalize()+', ')
            st = st[:-2]
            ans = ans + 'Half Damage from ' + st + '\n'
        if d200:
            st = ''
            for t in d200:
                st = st + (t.capitalize()+', ')
            st = st[:-2]
            ans = ans + 'Double Damage from ' + st + '\n'
        if d400:
            st = ''
            for t in d400:
                st = st + (t.capitalize()+', ')
            st = st[:-2]
            ans = ans + '4x Damage from ' + st + '\n'
        return ans

    def get_ability_text(self, api, ability_text, is_hidden = False):
        ability = api.get_ability(ability_text)
        flavor = ''
        flavor = ability.name.title().replace('-',' ')
        
        url_text = ability_text.title().replace('-','_')
        B_URL = 'https://bulbapedia.bulbagarden.net/wiki/' + url_text + '_%28Ability%29'
        
        flavor = '<a href="'+B_URL+'">'+flavor+'</a>'

        if is_hidden:
            flavor = flavor + ' (Hidden Ability)'
        flavor = flavor + '\n'
        for fte in ability.flavor_text_entries:
            if fte.language.name == 'en':
                flavor = flavor + fte.flavor_text + '\n'
                break
        flavor = flavor + '\n'
        return flavor

    def get_ability(self, api, query):
        response = ''
        try:
            pok = api.get_pokemon(query)
            response = 'List of abilities:' + '\n'
            response = response + '\n'
            for a in pok.abilities:
                response = response + self.get_ability_text(api, a.ability.name, a.is_hidden)
        except:
            try:
                response = get_ability_text(api, query)
            except:
                response = 'Invalid query'
        return response

    async def pokedexcmd(self, message):
        """It is a pokedex"""
        logger.debug("Init Pokedex")
        poke_client = pokepy.V2Client(cache='in_disk')
        logger.debug("PokeAPI Client acquired")
        response = ''
        args = utils.get_args_raw(message)
            
        if len(args) < 1:
            logger.debug("Random Pokemon")
            await utils.answer(message, 'No pokemon name given, getting a random pokemon...')
            await asyncio.sleep(3)
            query = random.randint(1,807)
            response = self.get_info(poke_client, query)
            await utils.answer(message, response)
        else:
            logger.debug("Pokemon "+args)
            input_name = self.parse_args(args) #Replacing white spaces with -
            response = self.get_info(poke_client, input_name)
            await utils.answer(message, response)

    