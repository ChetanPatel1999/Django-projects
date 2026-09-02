from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
