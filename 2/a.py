import json

f = open('data.json','r')

data = json.load(f)

name = data["name"]
age = data["age"]
city = data["city"]
print(f"name: {name} \nage: {age} \ncity: {city}")