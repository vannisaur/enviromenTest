from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def view_home(request):
    return render(request, 'recipes/pages/home.html', context={
        'nome': 'Gabriel Vanni',
        'idade': 23})


def visualizar(request):
    return HttpResponse('Texto')
