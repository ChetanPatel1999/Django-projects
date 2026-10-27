from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('get_token/',obtain_auth_token,name='get_token'),
    path("profile/",views.profile,name='profile'),
    path("admin_user/",views.adminUser,name='admin_user'),
]