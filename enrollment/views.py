from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer
from enrollment.permissions import IsStudent

class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset=Enrollment.objects.all()
    serializer_class=EnrollmentSerializer
    permission_classes=[IsStudent]

    def perform_create(self,serializer):
        serializer.save(student=self.request.user)