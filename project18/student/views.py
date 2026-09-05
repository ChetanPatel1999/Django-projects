from django.shortcuts import render,redirect
from .form import StudentForm
from .models import Student
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})
def student_create(request):
   form = StudentForm() 
   if request.method == 'POST':
       form = StudentForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('student:student_list') 
   return render(request, 'student/student_create.html', {'form': form})    