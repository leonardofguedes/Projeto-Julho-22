from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    if request.Post:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    form = RegisterForm
    return render(request, 'clients/pages/register_author.html', context={
        'form': form,
    })
