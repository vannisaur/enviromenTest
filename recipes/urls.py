from django.urls import path

from recipes.views import view_contato, view_home, view_sobre

urlpatterns = [
    path('', view_home),                # Home
    path('sobre/', view_sobre),         # /sobre/
    path('contato/', view_contato),     # /contato/
]
