from django.shortcuts import render
 
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def clientes(request):
    return render(request, "cliente/index.html")

def productos(request):
    return render(request, "productos/index.html")