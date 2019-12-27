# pokebot
Its on Telegram at [@Veg_Pokedex_Bot](https://t.me/Veg_Pokedex_Bot)

## Setup
1. Clone the repo.
2. Get your api token from [Botfather](https://t.me/Botfather)
3. Create an app in Heroku
4. Save the token in a Config Var (Environment variable) on Heroku by the name `API_TOKEN` 
5. Push the repo to Heroku and activate one dyno (free).

For more help refer to: https://github.com/Eldinnie/ptb-heroku-skeleton/blob/master/README.md
One difference is that I'm saving the API_TOKEN in the config and not a string in the python file.

It should respond to messages now.

## Credits
1. [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
2. [PokeAPI](https://pokeapi.co/) and its wrapper [pokepy](https://github.com/PokeAPI/pokepy)

