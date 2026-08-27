from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def studentForm(request):
    return render(request,"studentForm.html")

def addStudent(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        city=request.POST.get("city")
        description=request.POST.get("description")
        

        if name and age and city and description:
            Student.objects.create(
                name=name,
                age=age,
                city=city,
                description=description
            ) 
            return redirect("success")
        else:
             return HttpResponse("<h1>please enter all field data</h1>")
    return render(request,"studentForm.html")


def success(request):
    return render(request,"success.html")