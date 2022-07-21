from django.shortcuts import render, get_object_or_404
from petstore.models import *


def home_view(request):
    nome = 'HOME'
    animals = Animal.objects.all()
    return render(request, 'petstore/pages/home.html', context={
        'nome': nome,
        'animals': animals,
    })

def one_only_view(request, id):
    nome = 'SPECIAL ANIMAL'
    animal = get_object_or_404(Animal, pk=id)
    return render(request, 'petstore/pages/detail.html', context={
        'nome': nome,
        'animal': animal,
        'detail' : True,
    })

def theory(request, *args, **kwargs):
    animais = Animal.objects.all()
    polo = {'libelula': 'libelula'}
    return render(
        request,
        'petstore/pages/theory.html',
        context={
            'polo' : polo,
            'animais' : animais,
        }
    )
