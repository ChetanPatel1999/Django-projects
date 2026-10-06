from django.urls import path
from . import views
urlpatterns = [
    path("sending_email/",views.sending_email,name="sending_email"),
]
