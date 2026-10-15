from django.urls import path
from . import views
urlpatterns = [
    path('get_student/',views.get_student,name='get_student'),
    path('add_student/',views.add_student,name='add_student'),
    path('update_student/<int:pk>/',views.update_student,name='update_student'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student'),
]