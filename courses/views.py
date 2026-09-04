from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from courses.models import Course
from courses.serializers import CourseSerializer
from courses.permissions import IsAdminOrReadOnly



class CourseViewSet(viewsets.ModelViewSet):

    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[IsAdminOrReadOnly]