from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>this is home page</h1>")

def about(request):
    return HttpResponse("<h1>this is about page</h1>")

def product(request):
    return HttpResponse("<h1>this is product page</h1>")