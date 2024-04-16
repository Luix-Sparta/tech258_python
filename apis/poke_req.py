import requests
import json

poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/krokorok")
print(poke_req.json())

poke_data = json.loads(poke_req.text)
print((type(poke_data)))

print(poke_data["name"])
print(poke_data["height"])
