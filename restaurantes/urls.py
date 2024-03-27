from django.urls import path
from . import views


urlpatterns = [
    path('restaurantes/', views.home(), name='restaurantes'),
    path('registration/', views.login(), name='registration'),
]