from django.urls import path, include


urlpatterns = [
    path('', include('api.yasg')),
    path('estate/', include('api.autohub.endpoints')),
    path('estate/', include('api.auth.endpoints')),
]
