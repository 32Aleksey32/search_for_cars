from django.core.management.base import BaseCommand
from app.models import Car

from app.utils import get_random_location


class Command(BaseCommand):
    help = 'Обновляет локации всех машин'

    def handle(self, **kwargs):
        for car in Car.objects.all():
            car.location = get_random_location()
            car.save()
        self.stdout.write(self.style.SUCCESS('Локации машин успешно обновлены'))
