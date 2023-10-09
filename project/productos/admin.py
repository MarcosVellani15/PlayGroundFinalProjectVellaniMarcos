from django.contrib import admin
from . import models

admin.site.site_title = "Productos"
admin.site.site_header = "El Ático de Drake"

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
        "precio",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria_id",
        "nombre",
    )
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"