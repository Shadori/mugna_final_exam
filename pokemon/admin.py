from django.contrib import admin
from .models import Pokemon, PokemonType


class PokemonAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Details",
            {
                "fields": [
                    "pokemon_number",
                    "pokemon_name",
                    "pokemon_type",
                    "description",
                    "weight",
                    "height",
                ]
            },
        )
    ]
    list_display = [
        "pokemon_number",
        "pokemon_name",
        "description",
        "weight",
        "height",
    ]
    list_filter = ["pokemon_number"]
    search_fields = ["pokemon_name"]
    filter_horizontal = ["pokemon_type"]


class PokemonTypeAdmin(admin.ModelAdmin):
    fieldsets = [("Details", {"fields": ["element_name"]})]
    search_fields = ["element_name"]


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)
