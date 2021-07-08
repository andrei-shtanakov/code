import requests
import json

from docs.models import Planet
from docs.models import Character

def jprint(obj):
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)


def get_planets():
    planet_url = "https://swapi.dev/api/planets/"
    count = 0
    while planet_url != None:
        planet = requests.get(planet_url)
        planet_url = planet.json()["next"]
        for i in planet.json()["results"]:
            p = Planet(name=i["name"],
                gravity=i["gravity"],
                climate=i["climate"],
                terrain=i["terrain"],
                orbital_period=i["orbital_period"],
                rotation_period=i["rotation_period"],
                diameter=i["diameter"],
                planet_url=i["url"]
                )
            p.save()
            print(i["name"])
            count = +1
    return(count)

def get_people():
    people_url = "https://swapi.dev/api/people/"
    count = 0
    while people_url != None:
        people = requests.get(people_url)
        people_url = people.json()["next"]
        for i in people.json()["results"]:
            p = Character(name=i["name"],
                gender=i["gender"],
                height=i["height"],
                mass=i["mass"],
                hair_color=i["hair_color"],
                skin_color=i["skin_color"],
                eye_color=i["eye_color"],
                birth_year=i["birth_year"],
                homeworld=Planet.objects.get(planet_url=i["homeworld"])
                )
            p.save()
            print(i["name"])
            count = +1
    return(count)

def del_all_planets():
    Planet.objects.all().delete()


def del_all_people():
    Character.objects.all().delete()

