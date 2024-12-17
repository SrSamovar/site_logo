from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Teacher, Club
from .serializers import TeacherSerializer, ClubSerializer
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly


def check_id(request):
    some_id = request.data.get('id')
    if not some_id:
        return Response({'error': 'Отсутствует id'}, status=400)


class TeacherViewList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        check_id(request)
        teacher = get_object_or_404(Teacher, id=request.data.get('id'))
        teacher.delete()
        return Response(status=204)
    
    def patch(self, request):
        check_id(request)
        teacher = get_object_or_404(Teacher, id=request.data.get('id'))
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.data['id'] == request.data.get('id'):
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ClubViewList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        club = Club.objects.all()
        serializer = ClubSerializer(club, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        check_id(request)
        club = get_object_or_404(Club, id=request.data.get('id'))
        club.delete()
        return Response(status=204)

    def patch(self, request):
        check_id(request)
        club = get_object_or_404(Club, id=request.data.get('id'))
        serializer = ClubSerializer(club, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.data['id'] == request.data.get('id'):
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)
