from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login

from pokemon.forms import RegistrationForm, LoginForm


class HomeView(TemplateView):
    template_name = "pages/homepage.html"


class StartView(TemplateView):
    template_name = "pages/startpage.html"

    # def display_meta(request):
    #     values = request.META.items()
    #     html = []
    #     for k, v in values:
    #         html.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
    #     return HttpResponse(f"<table>{html}</table>\n")


class RegistrationView(View):
    template_name = "pages/registration.html"

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        template_name = "pages/registration.html"
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully Registered")
                return redirect("pages:registration")
            else:
                return redirect("pages:registration")
        return render(request, template_name, {"form": form})


class LoginView(View):
    template_name = "pages/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if form.is_valid():
                if user is not None:
                    if user.is_active:
                        login(request, user)

                        return render(
                            request, "pages/login.html", {"username": username}
                        )
                    else:
                        return HttpResponse("Username and password were incorrect")
            else:
                form = LoginForm()
            return render(request, "pages/login.html", {"form": form})
