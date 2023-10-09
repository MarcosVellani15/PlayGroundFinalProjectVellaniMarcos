from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("clientes/", views.clientes, name="clientes"),
    path("producto/", views.producto, name="producto"),
]



urlpatterns += staticfiles_urlpatterns()