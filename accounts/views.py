from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Hash du mot de passe (OBLIGATOIRE)
            user.set_password(form.cleaned_data["password"])
            user.save()

            messages.success(request, "Compte créé avec succès")
            return redirect("login")

        else:
            messages.error(request, "Formulaire invalide")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie")
                return redirect("home")
            else:
                messages.error(request, "Identifiants incorrects")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Déconnexion effectuée")
    return redirect("login")

def home_view(request):
    return render(request, "home.html")
