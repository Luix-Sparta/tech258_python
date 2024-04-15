import json

# parsing - converting a string into structured data

#.loads example

# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])

# loads example
path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
value = json["name"]

print(type(value))
print(value)

# json.load takes a file
# json.loads takes a string
