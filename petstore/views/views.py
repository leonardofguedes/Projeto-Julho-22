from django.shortcuts import render
from petstore.models import *


def home_view(request):
    nome = 'NOME'
    animals = Animal.objects.all()
    return render(request, 'petstore/pages/home.html', context={
        'nome': nome,
        'animals': animals,
    })

def one_only_view(request):
    nome = 'NOME COMPLETO AO CONTRÁRIO'
    animals = Animal.objects.all()
    return render(request, 'petstore/pages/home.html', context={
        'nome': nome,
        'animals': animals,
        'detail' : True,
    })
