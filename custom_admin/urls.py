from django.urls import path
from .views import CarsCreateView, CarsUpdateView, CarsDeleteView


urlpatterns = [
    path('delete/<int:pk>/', CarsDeleteView.as_view(), name='delete'),
    path('create/', CarsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CarsUpdateView.as_view(), name='update'),
]