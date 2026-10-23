from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public, name='public'),
    path('private/', views.private, name='private'),
]