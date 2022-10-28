from django.core.management.base import BaseCommand, CommandError

# from pokemon.models import Pokemon

import requests
import json
from urllib.request import urlopen


# # # get weight data
# name = input("enter pokemon name:\n")
# source = "https://pokeapi.co/api/v2/pokemon/"
# comp_source = f"{source}{name}"
# response = requests.get(comp_source).json()
# weight = response["weight"]
# print(weight)


# # # get height data
# name = input("enter pokemon name:\n")
# source = "https://pokeapi.co/api/v2/pokemon/"
# comp_source = f"{source}{name}"
# response = requests.get(comp_source).json()
# height = response["height"]
# print(height)

# # get types data
# name = input("enter pokemon name:\n")
# source = "https://pokeapi.co/api/v2/pokemon/"
# comp_source = f"{source}{name}"
# response = requests.get(comp_source).json()
# types = response["types"]
# numb_of_elem = len(types)
# type_list = []
# for num in range(numb_of_elem):
#     x = types[num]
#     y = x["type"]
#     z = y["name"]
#     type_list.append(z)

# print(type_list)


class Command(BaseCommand):
    help = "add and saves pokemon info from pokeapi to the database"
    pokemon_name = input("enter pokemon name:\n")
    source = "https://pokeapi.co/api/v2/pokemon/"
    complete_source = f"{source}{name}"
    response = requests.get(complete_source).json()

    def add_arguments(self, parser):
        parser.add_argument("pokemon_name", nargs="+", type=int)

    def save_weight(self, *args, **options):
        height = response["height"]
        print(height)

    def save_height(self, *args, **options):
        height = response["height"]
        print(height)

    def save_types(self, *args, **options):
        type_list = []
        for num in range(numb_of_elem):
            x = types[num]
            y = x["type"]
            z = y["name"]
            type_list.append(z)
