from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookies(request):
    response = HttpResponse("<h1>set cookies is succefully</h1>")
    response.set_cookie("theme","light",max_age=60*60*24*7)
    response.set_cookie("language","english")
    return response

def get_cookies(request):
    theme= request.COOKIES.get("theme")
    language= request.COOKIES.get("language")
    return HttpResponse(f"<h1>cookies theme : {theme} and language :{language}</h1>")


def delete_cookies(request):
    response = HttpResponse("<h1>delete cookies</h1>")
    response.delete_cookie("theme")
    response.delete_cookie("language")
    return  response
