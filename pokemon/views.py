from django.shortcuts import render
from .models import Pokemon, Entrenador, Gimnasio

def index(request):
    return render(request, 'index.html')

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def entrenador_list(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'entrenador_list.html', {'entrenadores': entrenadores})

def gimnasio_list(request):
    gimnasios = Gimnasio.objects.all()
    return render(request, 'gimnasio_list.html', {'gimnasios': gimnasios})