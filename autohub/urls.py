from django.urls import path
from .views import HomeTemplateView, CarsDetailView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('detail/<int:pk>/', CarsDetailView.as_view(), name='detail'),
]