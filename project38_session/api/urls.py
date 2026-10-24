from django.urls import path
from .views import blogList
urlpatterns = [
    path('blogs/',blogList,name='blog_list'), 
]