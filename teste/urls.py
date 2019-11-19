from django.urls import path
from teste.views import login
from teste.views import cadastro
from teste.views import senha

urlpatterns = [
    path('',login),
    path('cadastro',cadastro),
    path('senha',senha),
]