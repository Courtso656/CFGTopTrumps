import requests
import random
random_integer = random.randint(1, 151)
pokemon_number = random_integer
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])