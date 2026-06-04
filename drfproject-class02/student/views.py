from rest_framework.views import APIView, Response

from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.viewsets import (
    ModelViewSet
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

# concrete generic views 
# 1. ListCreateAPIView  # for listing all students and creating a new student.  -GET & POST requests
# 2. RetrieveUpdateDestroyAPIView  # for retrieving, updating, and deleting a specific student based.  -GET,PUT,DELETE requests



# all-students/  # GET request to list all students , POST request to create a new student
class StudentAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer





# class StudentAPIView(APIView):

#     def get(self, request):

#         students = Student.objects.all()

#         serializer = StudentSerializer(
#             students,
#             many=True
#         )

#         return Response(serializer.data)

#     def post(self, request):

#         serializer = StudentSerializer(
#             data=request.data
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.errors)
    




# api/students/1/ - GET, PUT, DELETE requests for student with pk=input
class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# class StudentDetailView(APIView):

#     def get(self, request, pk):

#         student = Student.objects.get(pk=pk)

#         serializer = StudentSerializer(student)

#         return Response(serializer.data)


#     def put(self, request, pk):

#         student = Student.objects.get(pk=pk)

#         serializer = StudentSerializer(
#             student,
#             data=request.data
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.errors)
    
#     def delete(self, request, pk):

#         student = Student.objects.get(pk=pk)

#         student.delete()

#         return Response({
#             'message': 'Student deleted successfully'
#         })




#  api/students/1/ - get, put,delete
# api/student/  - get,post

# viewsets
class StudentviewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# api/students - get,post
# api/students/1/ - get, put, delete


