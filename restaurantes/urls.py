from django.urls import path
from . import views

urlpatterns = [
    path('restaurantes/', views.restaurantes, name='restaurantes'),
]