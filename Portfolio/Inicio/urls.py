from django.urls import path
from django.contrib import admin
from .views import inicio, page_not_found_view

urlpatterns = [
    path('', inicio, name="inicio"),
]

handler404 = "Inicio.views.page_not_found_view"
