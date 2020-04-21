import requests
import random
format = input("Which game type?" )
if format == "Single Round":
    print("Loading new game")
    restart = input("Ready to start?" )
    while restart == "yes" and format == "Single Round":
        player_pokemon = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon)
        response = requests.get(url)
        p_pokemon = response.json()
        stat_dic = p_pokemon['stats']
        speed = stat_dic[int('0')]
        hp = stat_dic[int('5')]
        self_speed = speed['base_stat']
        self_hp = hp['base_stat']
        self_weight = p_pokemon['weight']
        self_height = p_pokemon['height']
        print("Player Pokemon")
        print(p_pokemon['name'])
        print("Height:")
        print(self_height)
        print("Weight:")
        print(self_weight)
        print("Speed:")
        print(self_speed)
        print("Heath:")
        print(self_hp)

        computer_pokemon = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(computer_pokemon)
        response = requests.get(url)
        c_pokemon = response.json()
        stat_dic = c_pokemon['stats']
        speed = stat_dic[int('0')]
        hp = stat_dic[int('5')]
        other_speed = speed['base_stat']
        other_hp = hp['base_stat']
        other_weight = c_pokemon['weight']
        other_height = c_pokemon['height']
        print(" ")
        print("Computer Pokemon")
        print(c_pokemon['name'])

        stat=input("Select Stat" )
        if stat == "hp":
            if self_hp >= other_hp:
                print (self_hp)
                print(other_hp)
                print("Its super effective")
                restart = input("Want to play again?" )
            else:
                print (self_hp)
                print(other_hp)
                print("Your pokemon fainted")
                restart = input("Want to play again?")
        elif stat == "speed":
            if self_speed >= other_speed:
                print(self_speed)
                print(other_speed)
                print("Its super effective")
                restart = input("Want to play again?")
            else:
                print(self_speed)
                print(other_speed)
                print("Your pokemon fainted")
                restart = input("Want to play again?")
        elif stat == "weight":
            if self_weight >= other_weight:
                print(self_weight)
                print(other_weight)
                print("Its super effective")
                restart = input("Want to play again?")
            else:
                print(self_weight)
                print(other_weight)
                print("Your pokemon fainted")
                restart = input("Want to play again?")
        elif stat == "height":

            if self_height >= other_height:
                print(self_height)
                print(other_height)
                print("Its super effective")
                restart = input("Want to play again?")
            else:
                print(self_height)
                print(other_height)
                print("Your pokemon fainted")
                restart = input("Want to play again?")
        else:
            print("Error")
    else:
        print("Thank you playing")