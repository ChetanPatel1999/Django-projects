from django.shortcuts import render

# Create your views here.
def course(reqest):
    return render(reqest,"course.html")