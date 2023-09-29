from django.urls import path

from . import views

app_name = 'cliente'

urlpatterns = [
    path('', views.index),
    path("crear/", views.crear, name="crear"),
    path("crear_pais/", views.crear_pais, name="crear_pais"),
    path("crear_compra/", views.crear_compra, name="crear_compra"),
]
