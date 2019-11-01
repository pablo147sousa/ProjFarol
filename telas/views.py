from django.shortcuts import render,HttpResponse

# Create your views here.
def paginaInicial(request):
    return render(request,"telas/home.html")
def contato(request):
    return render(request,"telas/contato.html")
def teste(request,name):
    return render(request,'telas/teste.html',{'pao':name})     