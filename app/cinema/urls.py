from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<slug:slug>/<slug:slug_video>', views.movie, name='movie'),
]