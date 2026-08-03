"""
URL configuration for porject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from student import views as studentViews


urlpatterns = [
    path('admin/', admin.site.urls),
    # all url mapping of student
    # path('student/index', studentViews.index , name="student-index"),
    # path('student/about/', studentViews.about , name="student-about"),
    # path('student/login/', studentViews.login , name="student-login"),
    # path('student/contact/', studentViews.contact , name="student-contact"),
    path('student/', include('student.urls')),
    path('course/', include('course.urls')),
]
