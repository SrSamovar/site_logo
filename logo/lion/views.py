from django.shortcuts import render
from .models import Teacher, Child, Club
# Create your views here.


def teacher_list_view(request):
    teacher = Teacher.objects.all()
    templates = 'base.html'
    context = {'teachers': teacher}
    return render(request, templates, context)
