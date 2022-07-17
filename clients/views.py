from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'clients/pages/register_author.html', context={
        'form': form,
    })

def register_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_from_data'] = POST
    form = RegisterForm(POST)
    return redirect('register')