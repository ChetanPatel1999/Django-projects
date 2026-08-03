from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='color:red'>Hello django how are you</h1>")

def about(request):
    a=12
    b=5
    c=a+b
    return HttpResponse(f"this about page = {c}")

