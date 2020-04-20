import requests
import random
player_pokemon = random.randint(1, 151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon)
response = requests.get(url)
pokemon = response.json()
stat_dic = pokemon['stats']
speed = stat_dic[int('0')]
print("Player Pokemon")
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
print(speed['base_stat'])

computer_pokemon = random.randint(1, 151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(computer_pokemon)
response = requests.get(url)
pokemon = response.json()
print(" ")
print("Computer Pokemon")
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])