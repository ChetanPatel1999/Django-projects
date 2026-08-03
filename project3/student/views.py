from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, this is the student index page.</h1>")

def student_detail(request, student_id):
    return HttpResponse(f"<h1>Details for student with ID: {student_id}</h1>")

def student_welcome(request, username):
    return HttpResponse(f"<h1>Welcome, {username}!</h1>")

def student_courses(request, **kwargs):
    course_id = kwargs['course_id']
    course_name = kwargs.get('course_name')
    course_duration = kwargs.get('duration')
    return HttpResponse(f"<h1>Courses id: {course_id},<br>Name: {course_name} <br>Duration: {course_duration}</h1>")

def student_pass_year(request, year):
    return HttpResponse(f"<h1>Student passed in the year: {year}</h1>")
