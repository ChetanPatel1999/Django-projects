from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class StudentAPI(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                student = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=404
                )

            serializer = StudentSerializer(student)
            return Response(serializer.data)

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=404
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=404
            )

        student.delete()
        return Response(status=204)