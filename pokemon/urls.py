"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    # pokemonlist_view,
    # pokemondetail_view,
    # typelist_view,
    # pokemonintypes,
    PokemonListView,
    PokemonDetailView,
    PokemonTypeListView,
    PokemonTypeDetailView,
    PokemonCreateView,
    PokemonUpdateView,
    PokemonDeleteView,
    SearchPokemonView,
)

app_name = "pokemon"

urlpatterns = [
    path("", PokemonListView.as_view(), name="pokemonlist"),
    path("<int:id>", PokemonDetailView.as_view(), name="pokemondetail"),
    path("types/", PokemonTypeListView.as_view(), name="pokemontypes"),
    path("types/<int:id>", PokemonTypeDetailView.as_view(), name="pokemonintype"),
    path("create", PokemonCreateView.as_view(), name="create"),
    path("update/<int:id>", PokemonUpdateView.as_view(), name="update"),
    path("delete/<int:id>", PokemonDeleteView.as_view(), name="delete"),
    path("search", SearchPokemonView.as_view(), name="search"),
]
