from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from . import models


def index(request):
    cliente = models.clientes.objects.all()

    return render(request, "cliente/index.html", {"clientes":cliente})