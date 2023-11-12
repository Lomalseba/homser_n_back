from django.shortcuts import render
from django.http import HttpResponse
from back.models import Student
from back.serializers import StudentSerializer
from back.models import User
from back.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(serializer.data)
        return Response(serializer.data)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)