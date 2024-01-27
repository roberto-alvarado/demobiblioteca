from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name="libros"),
    path('libroscategoria/', views.ListLibrosCategoria.as_view(), name="libroscategoria"),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"),
]
