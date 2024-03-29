from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.viewsets import ModelViewSet

from app.models import Car, Cargo, Location

from .filters import CargoFilter
from .serializers import (
    CargoDetailSerializer,
    CargoSerializer,
    CargoUpdateSerializer,
    CarSerializer,
    CarUpdateSerializer
)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            serializer = CarUpdateSerializer
        else:
            serializer = CarSerializer
        return serializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargoFilter

    def get_serializer_class(self):
        if self.action == 'update':
            serializer = CargoUpdateSerializer
        elif self.action == 'retrieve':
            serializer = CargoDetailSerializer
        else:
            serializer = CargoSerializer
        return serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Извлекаем ZIP-коды
            pick_up_zip_code = serializer.validated_data.pop('pick_up_zip_code')
            delivery_zip_code = serializer.validated_data.pop('delivery_zip_code')

            # Получаем локации или возвращаем ошибку, если одна из них не найдена
            try:
                pick_up_location = Location.objects.get(zip_code=pick_up_zip_code)
                delivery_location = Location.objects.get(zip_code=delivery_zip_code)
            except Location.DoesNotExist:
                return Response({"error": "Одна из локаций с таким ZIP кодом не найдена."}, status=HTTP_400_BAD_REQUEST)

            # Создаем груз с данными
            cargo = Cargo.objects.create(
                    pick_up_location=pick_up_location,
                    delivery_location=delivery_location,
                    **serializer.validated_data
                )

            return Response(self.get_serializer(cargo).data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
