from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import  forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect(settings.LOGIN_URL)
    return render(request, 'authentication/signup.html', context={'form': form})
 
#function to logout a user
def logout_user(request):
    logout(request)
    return redirect('login')