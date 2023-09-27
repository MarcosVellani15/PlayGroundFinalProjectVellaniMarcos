from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from . import models


def index(request):
    cliente = models.Cliente.objects.all()

    return render(request, "cliente/index.html", {"Cliente":cliente})