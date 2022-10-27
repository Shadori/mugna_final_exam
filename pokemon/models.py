from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    pokemon_number = models.IntegerField()
    pokemon_name = models.CharField("name", max_length=20)
    pokemon_type = models.ManyToManyField(
        "pokemon.PokemonType",
        related_name="pokemon",
    )
    description = models.TextField(
        default="Pokemon description unavailable", blank=True, null=True
    )
    weight = models.DecimalField(
        "Weight (in kilograms)", max_digits=20, decimal_places=2
    )
    height = models.DecimalField("Height (in meters)", max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse("pokemon:pokemondetail", kwargs={"id: self.id"})

    class Meta:
        verbose_name = "Pokemon"

    def __str__(self):
        return f"{self.pokemon_name}"


class PokemonType(models.Model):
    element_name = models.CharField("element_name", max_length=20)

    def get_absolute_url(self):
        return reverse("PokemonType:pokemonintype", kwargs={"id: self.id"})

    class Meta:
        verbose_name = "PokemonType"
        verbose_name_plural = "PokemonTypes"

    def __str__(self):
        return f"{self.element_name}"
