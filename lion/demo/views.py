from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Teacher, Club
from .serializers import TeacherSerializer, ClubSerializer
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
import logging

logger = logging.getLogger(__name__)


def check_id(request):
    some_id = request.data.get('id')
    if not some_id:
        logging.warning('ID not found in request.data')
        return Response({'error': 'id не найден'}, status=400)
    
def not_object(request):
    if not request:
        logging.warning('Request object is None')
        return HttpResponse('Отсутствует объект', status=404)


class TeacherViewList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        teacher = Teacher.objects.all()
        not_object(teacher)
        serializer = TeacherSerializer(teacher, many=True)
        logging.info('Teacher view list')
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Teacher saved')
            return Response(serializer.data, status=201)
        logging.error('Teacher is not saved', status=404)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        teacher = get_object_or_404(Teacher, id=request.data.get('id'))
        teacher.delete()
        logging.info('Teacher deleted')
        return Response(status=204)
    
    def patch(self, request):
        check_id(request)
        teacher = get_object_or_404(Teacher, id=request.data.get('id'))
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.data['id'] == request.data.get('id'):
                serializer.save()
                logging.info('Teacher is updated')
                return Response(serializer.data)
        logging.error('Teacher is not updated')
        return Response(serializer.errors, status=400)


class ClubViewList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        club = Club.objects.all()
        not_object(club)
        serializer = ClubSerializer(club, many=True)
        logging.info('Club view list')
        return Response(serializer.data)

    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Club saved')
            return Response(serializer.data, status=201)
        logging.error('Club is not saved', status=404)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        check_id(request)
        club = get_object_or_404(Club, id=request.data.get('id'))
        club.delete()
        logging.info('Club deleted')
        return Response(status=204)

    def patch(self, request):
        check_id(request)
        club = get_object_or_404(Club, id=request.data.get('id'))
        serializer = ClubSerializer(club, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.data['id'] == request.data.get('id'):
                serializer.save()
                logging.info('Club is updated')
                return Response(serializer.data)
        logging.error('Club is not updated')
        return Response(serializer.errors, status=400)
