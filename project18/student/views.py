from django.shortcuts import render,redirect,get_object_or_404
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

def student_delete(request, std_id):
    # student = Student.objects.get(id=std_id)
    student = get_object_or_404(Student, id=std_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student:student_list')
    return render(request, 'student/student_delete.html', {'student': student})

def student_detail(request, std_id):
    student = get_object_or_404(Student, id=std_id)
    return render(request, 'student/student_detail.html', {'student': student})

def student_update(request, std_id):
    student = get_object_or_404(Student, id=std_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    return render(request, 'student/student_create.html', {'form': form, 'student': student})