from typing import List

from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from api.utils import get_cars_info
from app.models import Car, Cargo, Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'city', 'state_name', 'zip_code', 'latitude', 'longitude')


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'location', 'number', 'load_capacity')
        read_only_fields = ('location',)


class CarUpdateSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'location')


class CargoSerializer(ModelSerializer):
    count_nearby_cars = SerializerMethodField()
    pick_up_location = LocationSerializer(read_only=True)
    delivery_location = LocationSerializer(read_only=True)
    pick_up_zip_code = CharField(write_only=True, label='Почтовый индекс места самовывоза')
    delivery_zip_code = CharField(write_only=True, label='Почтовый индекс места доставки')

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_count_nearby_cars(self, cargo) -> int:
        return get_cars_info(cargo).get('count_nearby_cars')


class CargoDetailSerializer(ModelSerializer):
    cars_with_distance = SerializerMethodField()
    pick_up_location = LocationSerializer(read_only=True)
    delivery_location = LocationSerializer(read_only=True)

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_location', 'delivery_location', 'weight', 'description', 'cars_with_distance')

    def get_cars_with_distance(self, cargo) -> List[dict]:
        return get_cars_info(cargo).get('cars_with_distance')


class CargoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('weight', 'description')
