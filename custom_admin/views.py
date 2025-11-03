from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CarsForm
import re
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from autohub.models import Cars


class CarsDeleteView(LoginRequiredMixin, DeleteView):
    model = Cars 
    template_name = 'custom_admin/delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CarsUpdateView(LoginRequiredMixin, UpdateView):
    model= Cars
    template_name = 'custom_admin/update.html'
    form_class = CarsForm
    context_object_name = 'cars'
    success_url = "/"

    def form_valid(self, form):
        form
        return super().form_valid(form)
    


class CarsCreateView(LoginRequiredMixin, CreateView):
    model = Cars
    template_name = 'custom_admin/create.html'
    form_class = CarsForm
    success_url = "/"

    def form_valid(self, form):
        form
        return super().form_valid(form)


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


# def car_create(request):
#     if request.method == 'POST':
#         form = CarsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Машина добавлена!')
#             return redirect('home')
#     else:
#         form = CarsForm()
#     return render(request, 'custom_admin/create.html', {'form': form})


def bissnes(request):
    return render(request, 'custom_admin/main.html')