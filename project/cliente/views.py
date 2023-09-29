from django.shortcuts import redirect, render
from django.http import HttpResponse

from . import forms, models

def index(request):
    cliente = models.clientes.objects.all()

    return render(request, "cliente/index.html", {"clientes":cliente})

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("http://127.0.0.1:8000")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form":form})

def crear_pais(request):
    if request.method == "POST":
        form = forms.PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000")
    else:
        form = forms.PaisForm()
    return render(request, "cliente/crear_pais.html", {"form":form})

def crear_compra(request):
    if request.method == "POST":
        form = forms.CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear_compra.html", {"form":form})