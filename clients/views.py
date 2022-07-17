from django.shortcuts import render


def register_view(request):
    nome = 'TESTE APP CLIENTS'
    return render(request, 'clients/pages/register_author.html', context={
        'nome': nome,
    })
