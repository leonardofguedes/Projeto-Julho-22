from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from clients.forms import LoginForm
from clients.forms.register_form import RegisterForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from petstore.models import Animal
from petstore.forms import AnimalForm

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
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário criado. Faça o login.')
        del(request.session['register_form_data'])
        return redirect(reverse('login'))

    return redirect('register')


def login_view(request):
    form = LoginForm()
    return render(request, 'clients/pages/login.html', {
        'form': form,
        'form_action': reverse('login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(login_url)


@login_required(login_url='login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('login'))

    logout(request)
    return redirect(reverse('login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    animals = Animal.objects.filter(
        author=request.user
    )
    return render(
        request,
        'clients/pages/dashboard.html',
        context={
            'animals': animals,
        }
    )

@login_required(login_url='login', redirect_field_name='next')
def dashboard_edit(request, id):
    animals = Animal.objects.filter(
        author=request.user,
        pk=id,
    ).first()

    if not animals:
        raise Http404()

    form = AnimalForm(
        data=request.POST or None,
        instance=animals
    )

    return render(
        request,
        'clients/pages/dashboard_animal.html',
        context={
            'animals': animals,
        }
    )