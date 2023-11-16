from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sanem(request):
    return HttpResponse('<h1>Day Dreamer</h1>')