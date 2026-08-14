from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"student/base.html")

def home(request):
    return render(request,"student/home.html")

def about(request):
    students = [ 
           {'name': 'Aman', 'dept': 'IT'}, 
           {'name': 'John', 'dept': 'IT'}, 
           {'name': 'Riya', 'dept': 'HR'},
           {'name': 'Ravi', 'dept': 'HR'},
            {'name': 'Sara', 'dept': 'Sales'}, 
           ]     
    
    std={
        "totalObtainMarks":320,
        "totalMarks":500
    }
    
    return render(request,"student/about.html",{"students":students,"std":std,"name":"ram"})
