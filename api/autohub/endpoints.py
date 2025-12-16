from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (cars_create, cars_detail, cars_list, brand_create, brand_detail, brand_list, 
                  body_create, body_detail, body_list, rent_list)
from .api import (transmission_create, transmission_detail, transmission_list, sale_create, sale_detail, 
                  sale_list, rent_create, rent_detail)
from .generic_api import (CarListCreateAPIView, CarDetailAPIView)


router = DefaultRouter()
router.register(r'cars', CarListCreateAPIView, basename='cars')
router.register(r'cars_detail', CarDetailAPIView, basename='cars-detail')
router.register(r'brand', brand_list, basename='brand')
router.register(r'body', body_list, basename='body')
router.register(r'transmission', transmission_list, basename='transmission')
router.register(r'sale', sale_list, basename='sale')
router.register(r'rent', rent_list, basename='rent')
router.register(r'brand_detail', brand_detail, basename='brand-detail')
router.register(r'body_detail', body_detail, basename='body-detail')
router.register(r'transmission_detail', transmission_detail, basename='transmission-detail')
router.register(r'sale_detail', sale_detail, basename='sale-detail')
router.register(r'rent_detail', rent_detail, basename='rent-detail')
router.register(r'cars_create', cars_create, basename='cars-create')
router.register(r'brand_create', brand_create, basename='brand-create')
router.register(r'body_create', body_create, basename='body-create')
router.register(r'transmission_create', transmission_create, basename='transmission-create')
router.register(r'sale_create', sale_create, basename='sale-create')
router.register(r'rent_create', rent_create, basename='rent-create')
router.register(r'cars/<int:pk>/', CarDetailAPIView, basename='cars-detail')
router.register(r'cars/', CarListCreateAPIView, basename='cars-list')



urlpatterns = [
    path('', include(router.urls))
    # path('cars/', cars_list, name='cars-list'),
    # path('cars_create/', cars_create, name='cars-create'),
    # path('cars_detail/<int:pk>', cars_detail, name='cars-detail'),
    # path('brand/', brand_list, name='brand-list'),
    # path('brand_create/', brand_create, name='brand-create'),
    # path('brand_detail/<int:pk>/', brand_detail, name='brand-detail'),
    # path('body/', body_list, name='body-list'),
    # path('body_create/', body_create, name='body-create'),
    # path('body_detail/<int:pk>', body_detail, name='body-detail'),
    # path('transmission/', transmission_list, name='transmission-list'),
    # path('transmission_create/', transmission_create, name='transmission-create'),
    # path('transmission_detail/<int:pk>', transmission_detail, name='transmission-detail'),
    # path('sale/', sale_list, name='sale-list'),
    # path('sale_create/', sale_create, name='sale-create'),
    # path('sale_detail/<int:pk>/', sale_detail, name='sale-detail'), 
    # path('rent/', rent_list, name='rent-list'),
    # path('rent_create/', rent_create, name='rent-create'),
    # path('rent_detail/<int:pk>/', rent_detail, name='rent-detail'),
    # path('api/cars/', CarListCreateAPIView.as_view(), name='api-cars-list-create'),
    # path('api/cars/<int:pk>/', CarDetailAPIView.as_view(), name='api-cars-detail'),
]