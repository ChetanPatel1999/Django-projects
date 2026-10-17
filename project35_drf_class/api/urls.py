from django.urls import path
from .views import studentListCreateAPIView,studentRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('students/', studentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', studentRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve-update-destroy'),
]
