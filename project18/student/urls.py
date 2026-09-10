from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_delete/<int:std_id>/', views.student_delete, name='student_delete'),
    path('student_detail/<int:std_id>/', views.student_detail, name='student_detail'),
    path('student_update/<int:std_id>/', views.student_update, name='student_update')
]