from django.contrib import admin
from .models import Cars, Sale, Rent, Transmission, Brand, Body
from django.utils.html import mark_safe


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo_preview")
    search_fields = ("name",)
    list_display_links = ("id", "name")

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="60" style="border-radius:6px;">')
        return "-"
    logo_preview.short_description = "Лого"


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "brand", "model",
        "price", "year", "body",
        "sale", "rent", "owner", "image_preview"
    )

    list_filter = (
        "brand", "body", "transmission",
        "year", "sale", "rent", "owner"
    )

    search_fields = ("name", "model", "color", "owner__username")

    readonly_fields = ("image_preview", "join_date")

    list_display_links = ("id", "name")

    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "brand", "model", "year", "price", "owner")
        }),
        ("Характеристики", {
            "fields": ("body", "color", "seats", "transmission")
        }),
        ("Продажа / Аренда", {
            "fields": ("sale", "rent")
        }),
        ("Описание", {
            "fields": ("description",)
        }),
        ("Фото", {
            "fields": ("picture", "image_preview")
        }),
        ("Служебное", {
            "fields": ("join_date",)
        }),
    )

    def image_preview(self, obj):
        if obj.picture:
            return mark_safe(
                f'<img src="{obj.picture.url}" width="120" style="border-radius:10px;">'
            )
        return "Нет фото"

    image_preview.short_description = "Превью"

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
