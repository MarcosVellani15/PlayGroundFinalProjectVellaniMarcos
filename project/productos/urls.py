from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    #path("comprar/", views.comprar, name="comprar"),
]



urlpatterns += staticfiles_urlpatterns()