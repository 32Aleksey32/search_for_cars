from django_filters.rest_framework import FilterSet, NumberFilter
from api.utils import get_cars_info
from app.models import Cargo


class CargoFilter(FilterSet):
    max_distance = NumberFilter(method='filter_by_max_distance', label="Дистанция до машины в милях")

    class Meta:
        model = Cargo
        fields = ['weight']

    def filter_by_max_distance(self, queryset, name, value):
        cargos = []
        for cargo in queryset:
            # Получаем машины с рассчитанной дистанцией до груза
            cars_with_distance = get_cars_info(cargo).get('cars_with_distance')
            # Проверяем, существует ли хотя бы одна машина, расстояние до которой меньше или равно указанному значению
            if any(car['distance_to_cargo'] <= value for car in cars_with_distance):
                cargos.append(cargo.id)
        # Фильтрация queryset по id грузов, удовлетворяющих условию
        return queryset.filter(id__in=cargos)
