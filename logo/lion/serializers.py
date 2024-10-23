from rest_framework import serializers

from .models import Teacher, Club


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'surname', 'first_name', 'last_name', 'work_experience', 'work_position']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'price']
