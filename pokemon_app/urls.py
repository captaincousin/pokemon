from django.urls import path
from pokemon.views import index, pokemon_list, entrenador_list, gimnasio_list
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pokemons/', pokemon_list, name='pokemon_list'),
    path('entrenadores/', entrenador_list, name='entrenador_list'),
    path('gimnasios/', gimnasio_list, name='gimnasio_list'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])