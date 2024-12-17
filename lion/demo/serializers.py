from rest_framework import serializers
from .models import Teacher, Child, Club


def validate_age(self, value):
    if value < 0:
        raise serializers.ValidationError('Возраст должен быть положительным')
    return value


class TeacherSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[validate_age])

    class Meta:
        model = Teacher
        fields = ['name', 'age', 'position']

    

class ChildSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[validate_age])

    class Meta:
        model = Child
        fields = ['name', 'age']


class ClubSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[validate_age])
    
    class Meta:
        model = Club
        fields = ['name', 'price']
