from django import forms
from .models import Utilisateur


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields=["username", "email", "password"]
        widgets = {
            'username': forms.CharField(max_length=14, 
                                        min_length=2, 
                                        required=True, 
                                        strip=True, 
                                        help_text="Nom d'utilisateur", 
                                        widget=forms.TextInput,
                                        label="Nom d'utilisateur"
                                        ),
            'email': forms.EmailField(max_length=254,
                                      min_length=10, 
                                      required=True, 
                                      strip=True, 
                                      help_text="Email", 
                                      widget=forms.EmailInput, 
                                      label="Email"
                                      ),
            'password': forms.CharField(max_length=50, 
                                        required=True, 
                                        strip=True, 
                                        help_text="Mot de passe", 
                                        widget=forms.PasswordInput, 
                                        label="Email"
                                        )
        }
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields=["email", "password"]
        widgets = {
                
            'email': forms.EmailField(max_length=254,
                                      min_length=10, 
                                      required=True, 
                                      strip=True, 
                                      help_text="Email", 
                                      widget=forms.EmailInput, 
                                      label="Email"
                                      ),
            'password': forms.CharField(max_length=50, 
                                        required=True, 
                                        strip=True, 
                                        help_text="Mot de passe", 
                                        widget=forms.PasswordInput, 
                                        label="Email"
                                        )
            }