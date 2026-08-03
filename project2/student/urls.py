from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index, name="student-index"),
    path("about/",views.about, name="student-about"),
    path("contact/",views.contact, name="student-contact"),
    path("login/",views.login, name="student-login"),
]
