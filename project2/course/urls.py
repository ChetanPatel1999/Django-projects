from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index, name="course-index"),
    path("about/",views.about, name="course-about"),
    path("contact/",views.contact, name="course-contact"),
    path("login/",views.login, name="course-login"),
]
