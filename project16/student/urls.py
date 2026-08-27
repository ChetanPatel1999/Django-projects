from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.studentForm, name="studentForm"),
    path('addStudent/',views.addStudent, name="addStudent"),
    path('success/',views.success, name="success")
    
]
