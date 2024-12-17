from django.urls import path
from .views import TeacherViewList


urlpatterns = [
    path('teachers/', TeacherViewList.as_view())
]
