from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurantes

# Create your views here.
def home(request):
    return  render (request, 'restaurantes.html')
