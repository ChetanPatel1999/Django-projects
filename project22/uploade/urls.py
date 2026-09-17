from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_files, name='display_files'),
    path('upload/', views.upload_file, name='upload_file'),
]   