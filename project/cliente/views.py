from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contexto = {"name" : "Cliente"}
    return render(request, "cliente/index.html", contexto)