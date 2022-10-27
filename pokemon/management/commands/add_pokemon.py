from django.core.management.base import BaseCommand, CommandError
from pokemon.models import Pokemon

import requests


class Command(BaseCommand):
    help = "add and saves pokemon info from pokeapi to the database"

    response = requests.get("https://pokeapi.co/api/v2/pokemon/{id or name}/")
    getdata = response.json()
