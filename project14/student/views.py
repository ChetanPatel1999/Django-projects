from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students = Student.objects.all()
    ujjain_students = Student.objects.filter(city="ujjain")
    context = {
        'students': students,
        'ujjain_students': ujjain_students 
    }
    return render(request,'home.html',context)