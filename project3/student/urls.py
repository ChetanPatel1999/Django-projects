from django.urls import path , re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student_welcome/<str:username>/', views.student_welcome, name='student_welcome'),
    path('student_courses/<int:course_id>/<str:course_name>/<str:duration>/', views.student_courses, name='student_courses'),
    re_path(r'^student_pass_year/(?P<year>[0-9]{4})/$', views.student_pass_year, name='student_pass_year'),  
]