from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        "name": "John Doe",
        "age": 30,
    }
    return JsonResponse(data)
