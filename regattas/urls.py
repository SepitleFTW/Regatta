from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("regattas/", include("regattas.url")),
    path("", views.index, name="index")
]