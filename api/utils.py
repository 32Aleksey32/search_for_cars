from geopy.distance import distance

from app.models import Car


def get_cars_info(cargo) -> dict:
    """Функция позволяет получить информацию о машинах с номером и дистанцией до конкретного груза"""
    cars_with_distance = []
    count = 0

    cargo_latitude = cargo.delivery_location.latitude
    cargo_longitude = cargo.delivery_location.longitude

    for car in Car.objects.all():
        # Вычисляем расстояние от груза до машины
        car_latitude = car.location.latitude
        car_longitude = car.location.longitude
        distance_miles = distance((cargo_latitude, cargo_longitude), (car_latitude, car_longitude)).miles

        # Если расстояние до машины меньше или равно 450, то увеличиваем счетчик автомобилей
        if distance_miles <= 450:
            count += 1

        cars_with_distance.append({
            'number': car.number,
            'distance_to_cargo': distance_miles
        })

    sorted_cars_with_distance = sorted(cars_with_distance, key=lambda x: x['distance_to_cargo'])

    return {'count_nearby_cars': count, 'cars_with_distance': sorted_cars_with_distance}
