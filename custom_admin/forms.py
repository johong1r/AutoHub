from django import forms
from django.forms import ModelForm
from autohub.models import Cars, Body, Brand, Transmission, Sale, Rent


class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = [
            'picture', 'name', 'brand', 'model', 'price',
            'body', 'color', 'seats', 'sale', 'rent',
            'transmission', 'year', 'description',
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "brand": forms.Select(attrs={
                'class': 'form-control',
            }),
            "model": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите модель',
            }),
            "price": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену',
            }),
            "body": forms.Select(attrs={
                'class': 'form-control',
            }),
            "color": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цвет',
            }),
            "seats": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество мест',
            }),
            "sale": forms.Select(attrs={
                'class': 'form-control',
            }),
            "rent": forms.Select(attrs={
                'class': 'form-control',
            }),
            "transmission": forms.Select(attrs={
                'class': 'form-control',
            }),
            "year": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год',
            }),
            "description": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
                'rows': 4,
            }),
        }
