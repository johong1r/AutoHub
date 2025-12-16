from django.urls import path
from .api import custom_login, custom_register

urlpatterns = [
    path('login/', custom_login, name='custom-login'),
    path('register/', custom_register, name='custom-register'),
]   