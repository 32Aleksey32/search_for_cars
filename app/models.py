from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, CharField, FloatField, ForeignKey, Model, PositiveIntegerField

from app.utils import generate_unique_number, get_random_location, validate_unique_number


class Location(Model):
    city = CharField(max_length=50, verbose_name='Город')
    state_name = CharField(max_length=50, verbose_name='Полное наименование штата')
    zip_code = CharField(max_length=5, verbose_name='Почтовый индекс')
    latitude = FloatField(verbose_name='Широта')
    longitude = FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'Локация c почтовым индексом № {self.zip_code}'


class Car(Model):
    number = CharField(
        unique=True,
        max_length=5,
        default=generate_unique_number,
        validators=[validate_unique_number],
        verbose_name='Номер'
    )
    location = ForeignKey(
        Location,
        default=get_random_location,
        on_delete=CASCADE,
        verbose_name='Текущая локация'
    )
    load_capacity = PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name='Грузоподъемность'
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'Машина № {self.id}'


class Cargo(Model):
    pick_up_location = ForeignKey(
        Location,
        on_delete=CASCADE,
        related_name='pick_up',
        verbose_name='Место самовывоза'
    )
    delivery_location = ForeignKey(
        Location,
        on_delete=CASCADE,
        related_name='delivery',
        verbose_name='Место доставки'
    )
    weight = FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name='Вес'
    )
    description = CharField(
        max_length=500,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return f'Груз № {self.id}'
