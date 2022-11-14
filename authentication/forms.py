from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        #pour les clients on aura besoin uniquement des champs etmail et password
        fields = ('username', 'email', 'password1', 'password2')