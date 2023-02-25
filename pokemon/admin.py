from django.contrib import admin
from .models import Pokemon, Entrenador, Gimnasio, Generacion

# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'nivel')

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'ciudad_natal')

@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'lider')

@admin.register(Generacion)
class GeneracionAdmin(admin.ModelAdmin):
    list_display = ('numero_generacion',)  # <--- lista de campos a mostrar en la tabla
    list_filter = ('numero_generacion',)  # <--- lista de campos a utilizar para filtrar la tabla
    search_fields = ('numero_generacion',)  # <--- lista de campos a utilizar para buscar la tabla