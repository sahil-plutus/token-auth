from rest_framework import serializers
from .models import Student
# from rest_framework.permissions import AllowAny

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'