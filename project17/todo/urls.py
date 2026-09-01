from django.urls import path
from . import views

# app_name = 'todo'

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
]
