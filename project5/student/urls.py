from django.urls import path
from . import views

urlpatterns=[
       path("student_list/",views.student_list,name="studen_list")
]