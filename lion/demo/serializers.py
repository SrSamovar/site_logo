from rest_framework import serializers
from .models import Teacher, Child, Club


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'position']


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name', 'age']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'price']
