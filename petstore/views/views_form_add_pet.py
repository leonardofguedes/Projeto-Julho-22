from django.shortcuts import render, redirect
from petstore.forms import AnimalForm
from django.http import Http404

def pet_view(request):
    form = AnimalForm
    return render(request, 'petstore/partials/add_animal.html', {
        'form': form,
    })

def pet_create(request):
    if not request.POST:
        raise Http404()
    form = AnimalForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return render(request, 'petstore/partials/add_animal.html',
                  {'form': form,
                   })