import json
import requests as req
import time 

def how_many_different_species_in_episode_6():
    url =  "https://swapi.dev/api/films/3"
    res = req.get(url)
    print (len(res.json()["species"]) + "個")


def sorting_the_movie_names():
    filmstitle = {} 
    url =  "https://swapi.dev/api/films/"

    res = req.get(url)
    for  film   in res.json()["results"]:
        title = film["title"]
        episode_id = film["episode_id"]
        filmstitle[f"Episode {episode_id}"] = title
    filmstitle = dict(sorted(filmstitle.items(), key=lambda x: x[0]))
    print(filmstitle)


def vehicles_with_more_than_1000_horsepower():
    vehicles = {}
    page = "1"
    while page is not None:
        url = f"https://swapi.dev/api/vehicles/?page={page}"
        res = req.get(url)

        for vehicle in res.json()["results"]:
            try:    
                if int(vehicle["max_atmosphering_speed"]) > 1000:
                    name = vehicle["name"]
                    speed = vehicle["max_atmosphering_speed"]
                    vehicles[name] = speed           
                else:
                    pass
            except ValueError:
                pass

        if res.json()["next"] is not None:
            page = res.json()["next"][-1]
        else:
            page = None
    print("cars are over 1000 is",len(vehicle))
