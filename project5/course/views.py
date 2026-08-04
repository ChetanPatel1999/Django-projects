from django.shortcuts import render

# Create your views here.
def course_list(request):
    #logic
    return render(request,"course/home.html")
