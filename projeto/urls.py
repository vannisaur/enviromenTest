"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


# HTTP Request
def view_home(request):
    return HttpResponse('Visualização da Página')
    # Return HTTP Response


def view_sobre(request):
    return HttpResponse('Página Sobre')


def view_contato(request):
    return HttpResponse('Página Contato')


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', view_home),          # Home
    path('sobre/', view_sobre),    # /sobre/
    path('contato/', view_contato),  # /contato/
]
