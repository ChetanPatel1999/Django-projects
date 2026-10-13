from django.urls import path
from . import views
urlpatterns = [
    path('channel_list/',views.channel_list,name='channel_list'),
    # path('cache_delete/',views.cache_delete,name='cache_delete'),
]