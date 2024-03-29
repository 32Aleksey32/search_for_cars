from django.contrib import admin

from app.models import Car, Cargo, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state_name', 'zip_code', 'latitude', 'longitude')
    search_fields = ('zip_code',)
    list_filter = ('state_name',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('pick_up_location', 'delivery_location', 'weight', 'description')
    search_fields = ('delivery_location', 'pick_up_location')
    list_filter = ('weight',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('number', 'location', 'load_capacity')
    search_fields = ('number',)
    list_filter = ('load_capacity',)
