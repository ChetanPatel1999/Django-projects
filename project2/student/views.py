from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this is student index page</h1>")

def about(req):
     return HttpResponse("<h1>this is student about page</h1>")

def login(req):
     
     return HttpResponse("<h1>this is student login page</h1>")

def contact(req):
     return HttpResponse("<h1>this is student contact page</h1>")