from django.urls import path
from . import views 
urlpatterns = [
    path('channel/', views.channel_list, name='channel_list'),
]