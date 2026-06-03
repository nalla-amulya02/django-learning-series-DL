from django.urls import path

from student.views import StudentAPIView


urlpatterns = [
    path('all-students/', StudentAPIView.as_view()),
    path('add-student/', StudentAPIView.as_view()),
]