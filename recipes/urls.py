from django.urls import path

from recipes.views import view_home, visualizar

urlpatterns = [
    path('', view_home),                # Home
    path('aba/', visualizar)
]
