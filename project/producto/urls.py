from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

app_name = "producto"

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index"), name="index"),
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/create/", login_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("producto/delete/<int:pk>", login_required(views.ProductoDelete.as_view()), name="producto_delete"),
    path("producto/update/<int:pk>", login_required(views.ProductoUpdate.as_view()), name="producto_update"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/create/", login_required(views.ProductoCategoriaCreate.as_view()), name="productocategoria_create"),
    path("productocategoria/update/<int:pk>", login_required(views.ProductoCategoriaUpdate.as_view()), name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", login_required(views.ProductoCategoriaDelete.as_view()), name="productocategoria_delete"),

]

urlpatterns += staticfiles_urlpatterns()