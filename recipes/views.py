# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'nome': 'Gabriel Vanni',
        'idade': 23})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'nome': 'Gabriel Vanni',
        'idade': 23})
