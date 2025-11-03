from django.urls import path
from .views import CarsCreateView, bissnes, user_login, user_register, CarsUpdateView, CarsDeleteView


urlpatterns = [
    path('delete/<int:pk>/', CarsDeleteView.as_view(), name='delete'),
    path('create/', CarsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CarsUpdateView.as_view(), name='update'),
    path('custom/', bissnes, name='custom'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
]