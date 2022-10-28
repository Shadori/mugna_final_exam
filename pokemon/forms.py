from django import forms

from .models import Pokemon, PokemonType
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"

    def clean_weight(self):
        pokemon_weight = self.cleaned_data.get("weight")
        if pokemon_weight <= 0:
            raise forms.ValidationError("Cannot enter negative or zero values!")

    def clean_height(self):
        pokemon_height = self.cleaned_data.get("height")
        if pokemon_height <= 0:
            raise forms.ValidationError("Cannot enter negative or zero values!")


class PokemonTypeForm(forms.ModelForm):
    class Meta:
        model = PokemonType
        fields = "__all__"


class PokemonUpdateForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            "pokemon_number",
            "pokemon_name",
            "pokemon_type",
            "description",
            "weight",
            "height",
        ]


class PokemonDeleteForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            "pokemon_number",
            "pokemon_name",
            "pokemon_type",
            "description",
            "weight",
            "height",
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class RegistrationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            "username",
            "password",
        ]
