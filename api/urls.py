from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CargoViewSet, CarViewSet


app_name = 'api'

router = DefaultRouter()

router.register('cargo', CargoViewSet, basename='cargo')
router.register('cars', CarViewSet, basename='cars')


urlpatterns = [
    path('', include(router.urls)),
]
