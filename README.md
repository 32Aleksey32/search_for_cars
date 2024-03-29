# API: Сервис поиска ближайших машин для перевозки грузов.

### О проекте:
Вы можете добавлять грузы, отслеживать сколько автомобилей находится рядом с каждым грузом (в пределах 450 миль),
отслеживать точное расстояние конкретного груза до каждого автомобиля, обновлять информацию о грузах и автомобилях, удалять грузы.
Доступен фильтр списка грузов по весу и по милям ближайших машин до грузов.
Так же локация каждого автомобиля автоматически обновляется каждые 3 минуты (локация меняется на другую случайную).

## Как запустить проект:

1. **Клонируйте репозиторий на свой компьютер.**
```
git clone https://github.com/32Aleksey32/search_for_cars.git
```

2. **Запустите процесс создания и запуск контейнеров:**
```
docker-compose up
```

3. **Перейдите на страницу http://localhost:8000**


###

<details>
<summary>ДОСТУПНЫЕ СТРАНИЦЫ</summary>
 
- ### Получение списка грузов:
  ```
  GET /cargo
  ```
  
  * Response
    ```json
    [
      {
        "id": 1,
        "count_nearby_cars": 7,
        "pick_up_location": {
            "id": 29989,
            "city": "Bagdad",
            "state_name": "Arizona",
            "zip_code": "86321",
            "latitude": 34.55367,
            "longitude": -113.08895
          },
        "delivery_location": {
            "id": 7954,
            "city": "Southside",
            "state_name": "West Virginia",
            "zip_code": "25187",
            "latitude": 38.72617,
            "longitude": -82.01878
          },
        "weight": 55.0,
        "description": "jkhjj"
      }
    ] 
    ```

- ### Получение информации о конкретном грузе:
  ```
  GET /cargo/{id}
  ```
  
  * Response 
    ``` json
    {
    "id": 1,
    "pick_up_location": {
        "id": 29989,
        "city": "Bagdad",
        "state_name": "Arizona",
        "zip_code": "86321",
        "latitude": 34.55367,
        "longitude": -113.08895
    },
    "delivery_location": {
        "id": 7954,
        "city": "Southside",
        "state_name": "West Virginia",
        "zip_code": "25187",
        "latitude": 38.72617,
        "longitude": -82.01878
    },
    "weight": 55.0,
    "description": "jkhjj",
    "cars_with_distance": [
        {
          "number": "2303Z",
          "distance_to_cargo": 206.1573416400788
        }
    ]
    }
    ```
    
- ### Создание груза
  ```
  POST /cargo/
  ```
  * Body
    ```json
    {
      "pick_up_zip_code": "50539",
      "delivery_zip_code": "50542",
      "weight": 150,
      "description": "Хрупкий груз"
    }
    ```

- ### Редактирование груза
  ```
  PUT /cargo/{id}/
  ```
  
  * Body
    ```json
    {
      "weight": 120.0,
      "description": "Просто описание"
    }
    ```

- ### Удаление груза
  ```
  DELETE /cargo/{id}/
  ```
  
- ### Получение списка машин:
  ```
  GET /cars
  ```
  * Response
    ```json
    [
      {
        "id": 1,
        "location": 7,
        "number": "9846M",
        "load_capacity": 11
      }
    ] 
    ```

- ### Получение информации о машине:
  ```
  GET /cars/{id}/
  ```
  
  * Response
    ``` json
    {
      "id": 5,
      "location": 15158,
      "number": "2860L",
      "load_capacity": 77
    }
    ```

- ### Создание машины:
  ```
  POST /cars/
  ```
  
  * Body
    ``` json
    {
      "number": "3526A",
      "load_capacity": 3
    }
    ```

- ### Редактирование машины:
  ```
  PUT /cars/{id}/
  ```
  
  * Body
  ``` json
    {
      "location": 6
    }
  ```

</details>

####

### Стек технологий использованный в проекте:
- Python 3.10
- Django 5.0.3
- Django Rest Framework 3.15.1
- geopy 2.4.1
- Docker
- PostgreSQL
