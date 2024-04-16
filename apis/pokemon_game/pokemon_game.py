import requests
import json
import random

#poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/krokorok")
ran = True

while ran is True:
    print("Base Form Pokemon Battle Game (ID or name):")
    user_pokemon = input("Input a Pokemon: ")

    poke_range = range(1,1026)
    user_pokemon_name_list = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1025")
    user_pokemon_name_list2 = user_pokemon_name_list.json()
    names = [pokemon["name"] for pokemon in user_pokemon_name_list2["results"]]
    #print(names)
    #print(len(names))
    #if type(user_pokemon) == int:
    #print(user_pokemon_name_list2)

    if user_pokemon.lower() in names or user_pokemon.isdigit() and int(user_pokemon) in poke_range :

        user_poke_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon}")
        user_pokemon_attack_stat = user_poke_req.json()["stats"][1]["base_stat"]
        user_pokemon_defence_stat = user_poke_req.json()["stats"][2]["base_stat"]

        #user_pokemon_name = " "
        user_pokemon_name = user_poke_req.json()["name"]
        #print(type(user_pokemon_name))
        print(f"User has selected: {user_pokemon_name.capitalize()}")
        print(f"User attack stat: {user_pokemon_attack_stat}")
        print(f"User defence stat: {user_pokemon_defence_stat}")

        comp_poke_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random.randint(1,len(names))}")
        comp_pokemon_name = comp_poke_req.json()["name"]
        comp_pokemon_attack_stat = comp_poke_req.json()["stats"][1]["base_stat"]
        comp_pokemon_defence_stat = comp_poke_req.json()["stats"][2]["base_stat"]

        print(f"Computer has selected: {comp_pokemon_name.capitalize()}")
        print(f"Computer attack stat: {comp_pokemon_attack_stat}")
        print(f"Computer defence stat: {comp_pokemon_defence_stat}")

        #print(user_pokemon_attack_stat)
        #print(comp_pokemon_attack_stat)

        dif_user_stats = user_pokemon_attack_stat - comp_pokemon_defence_stat
        dif_comp_stats = comp_pokemon_attack_stat - user_pokemon_defence_stat


        if dif_user_stats > dif_comp_stats:
            print(f"User has won!")
        elif dif_comp_stats > dif_user_stats :
            print("Computer has won!")
        else:
            print("There was a tie!")

        ran_condition = input("Do you want to play again, Yes or No? ")

        if ran_condition.upper() != "YES":
            ran = False
    else:
        print("Pokemon ID/Name not valid")
        ran = False
   # poke_count = requests.get("https://pokeapi.co/api/v2/pokemon")
    #print()


