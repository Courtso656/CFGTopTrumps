import requests
import random
print("Welcome to Top Dex!")
print(" -Single Round")
print(" -Multiple Rounds")
print(" -Build a Team")
print(" -Info")
format = input("Which game type?" )
if format == "Single Round":
    print("Loading new game")
    restart = "yes"
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
elif format == "Build a Team":
    print("Loading new game")
    restart = "yes"
    while restart == "yes" and format == "Build a Team":
        pokedex= []
        pokenumber= []
        player_pokemon1 = input("What pokemon would you like in slot 1? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        player_pokemon1 = input("What pokemon would you like in slot 2? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        player_pokemon1 = input("What pokemon would you like in slot 3? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        player_pokemon1 = input("What pokemon would you like in slot 4? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        player_pokemon1 = input("What pokemon would you like in slot 5? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        player_pokemon1 = input("What pokemon would you like in slot 6? (1-151)" )
        pokenumber.append(player_pokemon1)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
        response = requests.get(url)
        p_pokemon = response.json()
        pokedex.append(p_pokemon['name'])
        print( )
        print("Here's your pokemon team!")
        print(pokedex)
        print( )
        total_rounds = 0
        final_score = 0
        while restart =="yes" and total_rounds < 6:
            pokemon_select = input("Select your pokemon (Slot 1-6)" )
            list_no= int(pokemon_select)-1
            player_pokemon1 = pokenumber[list_no]
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon1)
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
                    total_rounds=total_rounds+1
                    final_score=final_score+1
                    print (self_hp)
                    print(other_hp)
                    print("Its super effective")
                    restart = input("Next Round?" )
                else:
                    total_rounds = total_rounds + 1
                    print (self_hp)
                    print(other_hp)
                    print("Your pokemon fainted")
                    restart = input("Next Round?" )
            elif stat == "speed":
                if self_speed >= other_speed:
                    total_rounds=total_rounds+1
                    final_score=final_score+1
                    print(self_speed)
                    print(other_speed)
                    print("Its super effective")
                    restart = input("Next Round?")
                else:
                    total_rounds=total_rounds+1
                    print(self_speed)
                    print(other_speed)
                    print("Your pokemon fainted")
                    restart = input("Next Round?")
            elif stat == "weight":
                if self_weight >= other_weight:
                    total_rounds = total_rounds + 1
                    final_score=final_score+ 1
                    print(self_weight)
                    print(other_weight)
                    print("Its super effective")
                    restart = input("Next Round?")
                else:
                    total_rounds = total_rounds + 1
                    print(self_weight)
                    print(other_weight)
                    print("Your pokemon fainted")
                    restart = input("Next Round?")
            elif stat == "height":

                if self_height >= other_height:
                    total_rounds = total_rounds + 1
                    fianl_score=final_score+ 1
                    print(self_height)
                    print(other_height)
                    print("Its super effective")
                    restart = input("Next Round?")
                else:
                    total_rounds = total_rounds + 1
                    print(self_height)
                    print(other_height)
                    print("Your pokemon fainted")
                    restart = input("Next Round?")
            else:
                print("Error")
        else:
            restart ="no"
            print ("Here's your final score!")
            print(final_score)
    else:
        print("Thank you playing")