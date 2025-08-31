from django.contrib import admin
from .models import CarMake, CarModel


# --- Inline: omogućuje dodavanje/uređivanje CarModel-a na stranici CarMake-a ---
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1
    fields = ("name", "type", "year", "dealer_id")
    show_change_link = True


# --- Pojedinačni admin za CarModel (lista, filteri, pretraga) ---
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "type", "year", "dealer_id")
    list_filter = ("car_make", "type", "year")
    search_fields = ("name", "car_make__name")
    autocomplete_fields = ("car_make",)


# --- Admin za CarMake s inline CarModel-ima ---
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "description")
    search_fields = ("name", "country")
    inlines = [CarModelInline]
