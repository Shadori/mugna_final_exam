from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    View,
)
from django.contrib import messages
from django.urls import reverse

from .models import Pokemon, PokemonType
from .forms import PokemonForm, PokemonType, PokemonUpdateForm, PokemonDeleteForm


class PokemonListView(View):
    model = Pokemon
    queryset = Pokemon.objects.all()
    context_object_name = "pokemon"
    template_name = "pokemon/pokemonlist.html"

    def get(self, request, *args, **kwargs):
        context = {"pokemon_list": self.queryset}
        return render(request, self.template_name, context)


class PokemonDetailView(View):
    model = Pokemon
    context_object_name = "pokemon"
    template_name = "pokemon/pokemondetail.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_detail = get_object_or_404(Pokemon, id=id)
        context = {"pokemon_detail": pokemon_detail}
        return render(request, self.template_name, context)


class PokemonTypeListView(ListView):
    model = PokemonType
    queryset = PokemonType.objects.all()
    context_object_name = "pokemontype"
    template_name = "pokemon/typelist.html"

    def get(self, request, *args, **kwargs):
        context = {"pokemon_types": self.queryset}
        return render(request, self.template_name, context)


class PokemonTypeDetailView(DetailView):
    model = PokemonType
    context_object_name = "pokemontype"
    template_name = "pokemon/pokemonintypes.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_type = get_object_or_404(PokemonType, id=id)
        context = {"pokemon_type": pokemon_type}
        return render(request, self.template_name, context)


"""ADDING POKEMON"""


class PokemonCreateView(View):
    model = Pokemon
    queryset = Pokemon.objects.all()
    context_object_name = "pokemon"
    template_name = "pokemon/createpokemon.html"

    def get_object(self):
        return None

    def get(self, request, *args, **kwargs):
        # GET method
        form = PokemonForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            form = PokemonForm()
        context = {"form": form}
        return render(request, self.template_name, context)


"""UPDATING POKEMON"""


class PokemonUpdateView(View):
    form_class = PokemonUpdateForm
    initial = {"key": "value"}
    template_name = "pokemon/updatepokemon.html"

    def get(self, request, id, *args, **kwargs):
        # GET method
        update_pokemon = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=update_pokemon)
        return render(request, self.template_name, {"form": form})

    def post(self, request, id=None, *args, **kwargs):
        # POST method
        update_pokemon = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=update_pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated!")
            return redirect("pokemon:update-pokemon-form", update_pokemon.id)

        return render(request, self.template_name, {"form": form})


"""DELETING POKEMON"""


class PokemonDeleteView(View):
    form_class = PokemonDeleteForm
    initial = {"key": "value"}
    template_name = "pokemon/deletepokemon.html"

    def get(self, request, id, *args, **kwargs):
        # GET method
        delete_pokemon = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=delete_pokemon)
        return render(request, self.template_name, {"form": form})

    def post(self, request, id=None, *args, **kwargs):
        # POST method
        delete_pokemon = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=delete_pokemon)
        if form.is_valid():
            delete_pokemon.delete()
            messages.success(request, "Successfully deleted!")
            return redirect("pokemon:update-pokemon-form", delete_pokemon.id)

        return render(request, self.template_name, {"form": form})


"""SEARCH FOR POKEMON"""


class SearchPokemonView(View):
    form_class = PokemonForm
    initial = {"key": "value"}
    template_name = "pages/pokemonsearch.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        errors = []
        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                errors.append("Enter a search term.")
            elif len(query) > 20:
                errors.append("Please enter at most 20 characters")
            else:
                pokemon = Pokemon.objects.filter(pokemon_name__icontains=query)
            return render(
                request,
                "pages/pokemonsearchresult.html",
                {"pokemon": pokemon, "query": query},
            )
        return render(request, "pages/pokemonsearch.html", {"errors": errors})
