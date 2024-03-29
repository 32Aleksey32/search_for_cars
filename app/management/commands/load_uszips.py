import csv

from django.core.management.base import BaseCommand

from app.models import Location
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Добавление локаций в БД'

    def handle(self, **kwargs):
        file = f'{BASE_DIR}/app/management/uszips.csv'
        try:
            with open(file, 'r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Location.objects.get_or_create(
                        zip_code=row['zip'],
                        latitude=row['lat'],
                        longitude=row['lng'],
                        city=row['city'],
                        state_name=row['state_name'],
                    )
            self.stdout.write(self.style.SUCCESS('Локации успешно добавлены в БД.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR("Ошибка: %s" % e))
