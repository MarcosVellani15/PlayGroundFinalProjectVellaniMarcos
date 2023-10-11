from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from.import models, forms

class ProductoCategoriaList(ListView, LoginRequiredMixin):
    model = models.ProductoCategoria

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            query = self.request.GET.get("buscar")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=query)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria

class ProductoCategoriaCreate(CreateView, LoginRequiredMixin):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDelete(DeleteView, LoginRequiredMixin):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoList(ListView, LoginRequiredMixin):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            query = self.request.GET.get("buscar")
            object_list = models.Producto.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list
    
class ProductoDetail(DetailView):
    model = models.Producto

class ProductoCreate(CreateView, LoginRequiredMixin):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

class ProductoDelete(DeleteView, LoginRequiredMixin):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")

class ProductoUpdate(UpdateView, LoginRequiredMixin):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")