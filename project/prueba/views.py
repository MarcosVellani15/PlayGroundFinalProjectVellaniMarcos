from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contexto = {"name" : "Mi nombre es Marcos Vellani"}
    return render(request, "prueba/index.html", contexto)