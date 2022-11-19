from django.core.management.base import BaseCommand, CommandError

# from pokemon.models import Pokemon

import requests

# import json


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
    # help = "add and saves pokemon info from pokeapi to the database"
    # pokemon_name = input("enter pokemon name:\n")
    # source = "https://pokeapi.co/api/v2/pokemon/"
    # complete_source = f"{source}{pokemon_name}"
    # response = requests.get(complete_source).json()

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="add pokemon info")

        # pass pokemon names

    def handle(self, *args, **options):
        pokemon_name = options["name"]
        source = "https://pokeapi.co/api/v2/pokemon/"
        complete_source = f"{source}{pokemon_name}"
        response = requests.get(complete_source).json()
        height = int(response["height"])
        weight = int(response["weight"])
        pokedex_number = int(response["id"])
        types = response["types"]
        type_list = []
        numb_of_elem = len(types)
        for num in range(numb_of_elem):
            x = types[num]
            pokemon_type = x["type"]
            pokemon_types = pokemon_type["name"]
            type_list.append(pokemon_types)

        print(pokemon_name.title())
        print(f"{height/10}" + " meters")
        print(f"{weight/10}" + " kgs")
        print(type_list)
        print(pokedex_number)

    # def save_weight(self, *args, **options):
    #     weight = response["weight"]
    #     print(height)

    # def save_height(self, *args, **options):
    #     height = response["height"]
    #     print(height)

    # def save_types(self, *args, **options):
    #     type_list = []
    #     for num in range(numb_of_elem):
    #         x = types[num]
    #         y = x["type"]
    #         z = y["name"]
    #         type_list.append(z)
