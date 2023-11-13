from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', status=200, context={
        'nome': 'Lucas'
    })
    # return http response


def contato(request):
    return HttpResponse('contato')
    # return http response


def sobre(request):
    return HttpResponse('sobre')
    # return http response
