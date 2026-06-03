from rest_framework.views import APIView, Response

from student.models import Student
from student.serializers import StudentSerializer
class StudentAPIView(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)