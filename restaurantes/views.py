from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def restaurantes(request):
    return HttpResponse("Hello, world. You're at the restaurantes index.")
