import json

f = open('film.json','r')

data = json.load(f)

revenue = 0
year = data[0]["year"]
last_film = data[0]
for film in data:
    revenue += film["revenue"]
    if year < film["year"]:
        year = film["year"]
        last_film = film

print(f"total revenue: {revenue}")
print(f"-last film-\ntitle: {last_film['title']}\nyear: {last_film['year']}\ndirector: {last_film['director']}\nrevenue: {last_film['revenue']}")