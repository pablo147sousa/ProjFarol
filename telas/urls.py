from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.paginaInicial),
    path('contato/',views.contato),
]