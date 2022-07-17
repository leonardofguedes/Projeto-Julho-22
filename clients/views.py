from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm
    return render(request, 'clients/pages/register_author.html', context={
        'form': form,
    })
