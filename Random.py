import requests
import random
format=input("Which game type?" )
if format == "Single Round":
    print("Loading new game")
    player_pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon)
    response = requests.get(url)
    p_pokemon = response.json()
    stat_dic = p_pokemon['stats']
    speed = stat_dic[int('0')]
    hp = stat_dic[int('5')]
    print("Player Pokemon")
    print(p_pokemon['name'])
    print("Height:")
    print(p_pokemon['height'])
    print("Weight:")
    print(p_pokemon['weight'])
    print("Speed:")
    print(speed['base_stat'])
    print("Heath:")
    print(hp['base_stat'])

    computer_pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(computer_pokemon)
    response = requests.get(url)
    c_pokemon = response.json()
    c_pokemon = response.json()
    stat_dic = c_pokemon['stats']
    speed = stat_dic[int('0')]
    hp = stat_dic[int('5')]
    print(" ")
    print("Computer Pokemon")
    print(c_pokemon['name'])

