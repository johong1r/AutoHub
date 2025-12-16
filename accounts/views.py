from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from custom_admin.forms import CarsForm
import re
from django.contrib.auth.models import User

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'custom_admin/register.html')


def user_login(request):
    form = CarsForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Неверный логин или пароль!")
    return render(request, 'custom_admin/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')