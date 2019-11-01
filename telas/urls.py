from django.urls import path
from . import views
urlpatterns = [
    path('',views.paginaInicial),
    path('contato/',views.contato),
    path('<str:name>/',views.teste),
]