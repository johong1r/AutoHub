from django.contrib import admin

from .models import Cars, Sale, Rent, Transmission, Brand, Body


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model', 'price', 'year']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ['name']