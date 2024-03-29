import csv

from django.core.management.base import BaseCommand

from app.models import Car
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Добавление машин в БД'

    def handle(self, **kwargs):
        file = f'{BASE_DIR}/app/management/cars.csv'
        try:
            with open(file, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Car.objects.get_or_create(
                        number=row['number'],
                        load_capacity=row['load_capacity'],
                    )
            self.stdout.write(self.style.SUCCESS('Машины успешно добавлены в БД.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR("Ошибка: %s" % e))
