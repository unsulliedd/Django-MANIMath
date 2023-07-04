from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from rest_framework.authtoken.models import Token
from .forms import *

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Token.objects.get_or_create(user=user)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'MANIMath_Account/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                Token.objects.get_or_create(user=user)
                
                remember_me = request.POST.get('remember_me')
                if remember_me:
                    request.session.set_expiry(None)  # Persistent cookie
                else:
                    request.session.set_expiry(0)

                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'MANIMath_Account/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')
