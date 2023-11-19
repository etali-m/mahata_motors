from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


#Formulaire de connexion
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(
        attrs={
            'class': 'form-control login-input', 
            'id':'username'
        }
    ))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control login-input',
            'id':'password'
        }
    ))


#Formulaire d'inscription     
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control login-input',
            'id': 'first_name', 
            'placeholder': 'Entrez votre nom'
        }
    ))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control login-input',
            'id': 'last_name',
            'placeholder': 'Entrez votre prénom'
        }
    ))
    email = forms.CharField(max_length=63, widget=forms.EmailInput(
        attrs={
            'class': 'form-control login-input',
            'id': 'email',
            'placeholder': 'Entrez votre e-mail'
        }
    ))
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control login-input',
            'id': 'password1',
            'placeholder': 'Entrez votre mot de passe'
        }
    ))
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control login-input',
            'id': 'password2',
            'placeholder': 'Confirmer le mot de passe'
        }
    ))
    numero_telephone = forms.CharField(max_length=17, widget=PhoneNumberPrefixWidget(
        attrs={
            'class': 'form-control login-input',
            'placeholder': 'Numéro de téléphone'
        },  
    ))

    class Meta(UserCreationForm.Meta):
        model = User

        # Inclure tous les champs requis pour le formulaire
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'numero_telephone')
