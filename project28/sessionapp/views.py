from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session["user"]="ram sharma"
    request.session["course"]="python"
    return HttpResponse("<h1>save session data succesfully</h1>")

def get_session(request):
    data1=request.session.get("user")
    data2=request.session.get("course")
    return HttpResponse(f"your name {data1} your course {data2}")

def delete_session(request):
#    del request.session["user"]
     request.session.flush()
     return HttpResponse("<h1>data delete succefully </h1>")