from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is course index page")

def about(req):
     return HttpResponse("<h1>this is course about page</h1>")

def login(req):
     
     return HttpResponse("<h1>this is course login page</h1>")

def contact(req):
     return HttpResponse("<h1>this is course contact page</h1>")
