from django.urls import path

from student.views import StudentAPIView, StudentDetailView, StudentviewSet

from rest_framework.routers import DefaultRouter

# Routers and ViewSets
router = DefaultRouter()

router.register('students', StudentviewSet) #-  #students/,  students/pk - get, post, put, delete requests for all students and specific student based on pk

urlpatterns = router.urls

    # path('students/', StudentAPIView.as_view()),


    # should be able to handle get, put, delete requests for a specific student 
    # based on their primary key (pk)
    # path('students/<int:pk>/', StudentDetailView.as_view()),

    # api/students/1/  # GET, PUT, DELETE requests for student with pk=1
    # path('students/<int:pk>/', StudentDetailView.as_view()),

