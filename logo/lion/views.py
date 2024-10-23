from django.shortcuts import render
from .models import Teacher, Child, Club
# Create your views here.


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    templates = 'teacher.html'
    context = {'teachers': teachers}
    return render(request, templates, context)


def clubs_list_view(request):
    clubs = Club.objects.all()
    templates = 'club.html'
    context = {'clubs': clubs}
    return render(request, templates, context)
