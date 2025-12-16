from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from autohub.models import Cars
from .serializer import CarModelSerializer
from .permission import CarsPermission


class CarListCreateAPIView(ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [CarsPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [CarsPermission]