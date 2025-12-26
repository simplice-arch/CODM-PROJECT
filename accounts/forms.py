from django import forms
from .models import Utilisateur

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        max_length=14,
        min_length=8,
        required=True,
        help_text="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Nom d'utilisateur"}),
        label="Nom d'utilistaeur"
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Email",
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
        label="Email"
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        help_text="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Mot de passe'}),
        label="Mot de passe"
    )
    class Meta:
        model = Utilisateur
        fields = ["username", "email", "password"]
       
       
       

class LoginForm(forms.Form):
    
    username = forms.CharField(
        max_length=14,
        min_length=8,
        required=True,
        help_text="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Nom d'utilisateur"}),
        label="Nom d'utilistaeur"
    )
     
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Mot de passe'}),
        label="Mot de passe"
    )
   

    class Meta:
        model = Utilisateur
        fields = ["username", "password"]
