from django_filters import FilterSet, CharFilter, NumberFilter
from autohub.models import Cars, Body, Brand, Sale, Rent, Transmission

class CarsFilter(FilterSet):
    price_gte = NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = NumberFilter(field_name='price', lookup_expr='lte')
    seats_gte = NumberFilter(field_name='seats', lookup_expr='gte')
    seats_lte = NumberFilter(field_name='seats', lookup_expr='lte')
    year = NumberFilter(field_name='rooms_count', lookup_expr='gte')
    year = NumberFilter(field_name='rooms_count', lookup_expr='lte')

    class Meta:
        model = Cars
        fields = []


class BodyFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Body
        fields = ['name']


class BrandFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = ['name']


class SaleFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Sale
        fields = ['name']


class RentFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Rent
        fields = ['name']


class TransmissionFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Transmission
        fields = ['name']