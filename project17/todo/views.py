from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
# Create your views here.
def show_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task.html', {'tasks': tasks})

def toggle_task(request, task_id):
    # task = Task.objects.get(id=task_id)
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todo:show_tasks')

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')   
        if title and description:
            Task.objects.create(title=title, description=description)
            return redirect('todo:show_tasks')
        return render(request, 'todo/add_task.html', {'error': 'Please provide both title and description.'})   
    return render(request, 'todo/add_task.html')