from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

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

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=63, widget=forms.TextInput(
            attrs={
                'class': 'form-control login-input', 
                'id':'username'
            }
        ))
    email = forms.CharField(max_length=63, widget=forms.EmailInput(
            attrs={
                'class': 'form-control login-input', 
                'id':'email'
            }
        ))
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-input', 
                'id':'password1'
            }
        ))
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-input', 
                'id':'password2'
            }
        ))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

        #pour les clients on aura besoin uniquement des champs etmail et password
        fields = ('username', 'email', 'password1', 'password2')