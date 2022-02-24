from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication 
from .models import Student
from .auth import CustomAuthToken
from rest_framework.permissions import IsAdminUser



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
