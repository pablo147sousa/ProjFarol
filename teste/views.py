from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def login(request):
    return render(request,'teste/telalogin.html')
  
def senha(request):
    return render(request,'teste/telasenha.html')
  
def cadastro(request):
    return render(request,'teste/telacadastro.html')
    