from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import StandardResultsSetPagination
from autohub.models import Cars, Transmission, Body, Brand, Sale, Rent
from .serializer import (
    CarSerializer,
    TransmissionSerializer,
    BodySerializer,
    BrandSerializer,
    SaleSerializer,
    RentSerializer,
    CarsDetailSerializer,
    CarsCreateUpdateSerializer
)
from .filters import CarsFilter, TransmissionFilter, BodyFilter, BrandFilter, SaleFilter, RentFilter


class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarsFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CarsDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return CarsCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
    

class TransmissionViewSet(ReadOnlyModelViewSet):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TransmissionFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TransmissionSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return TransmissionSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class BodyViewSet(ReadOnlyModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BodyFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BodySerializer
        elif self.action in ["create", "update", "partial_update"]:
            return BodySerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class BrandViewSet(ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BrandFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BrandSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return BrandSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class SaleViewSet(ReadOnlyModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SaleFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SaleSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return SaleSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()


class RentViewSet(ReadOnlyModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RentFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RentSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return RentSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()