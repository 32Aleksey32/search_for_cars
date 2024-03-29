import re
from random import choice, randint
from string import ascii_uppercase

from django.core.exceptions import ValidationError


def get_random_location():
    from app.models import Location
    return Location.objects.order_by('?').first()


def generate_unique_number():
    from app.models import Car
    unique_number_found = False
    while not unique_number_found:
        # Генерируем случайный номер по заданным правилам
        potential_number = f"{randint(1000, 9999)}{choice(ascii_uppercase)}"
        # Проверяем, не существует ли уже машина с таким номером в базе данных
        if not Car.objects.filter(number=potential_number).exists():
            unique_number_found = True
    return potential_number


def validate_unique_number(value):
    if not re.match(r'^[1-9]\d{3}[A-Z]$', value):
        raise ValidationError(
            'Уникальный номер должен иметь 4 цифры (от 1000 до 9999),'
            ' а после них - заглавная буква английского алфавита'
        )
