from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("clientes/", views.clientes, name="clientes"),
    path("producto/", views.producto, name="producto"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
]



urlpatterns += staticfiles_urlpatterns()