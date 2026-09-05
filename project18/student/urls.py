from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
]