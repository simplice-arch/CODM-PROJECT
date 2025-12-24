from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.password = make_password(form.cleaned_data["password"])
            utilisateur.save()
            return redirect("login")
        else:
            form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            utilisateur = authenticate(request, email=email, password=password)
            if utilisateur is not None:
                login(request, utilisateur)
                messages.success("Connexion Rétablie")
                return redirect("home")
            else:
                messages.error(request, "Identifiants Incorrects")
    return render(request, "login.html", {"form": form})


def home(request):
    return render(request, "home.html")