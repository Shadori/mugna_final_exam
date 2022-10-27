from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "pages/homepage.html", {})


def registration_view(*args, **kwargs):
    return HttpResponse("<h1>Registration Page</h1>")


def login_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def searchpokemon_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
