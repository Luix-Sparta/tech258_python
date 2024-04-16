import requests
import json

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
print(type(json_body))
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, json={"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})

print(post_multi_req.json()["result"])

# data= -> accepts a string (so we had to use json.dumps first)
# json= -> accepts a python dictionary
