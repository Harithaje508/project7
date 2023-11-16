from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def situmo(request):
    return HttpResponse('<h1>Put Your head on my shoulder</h1>')