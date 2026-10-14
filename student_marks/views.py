from django.shortcuts import render
from rest_framework import generics
from .models import StudentMarks
from .serializers import StudentMarkSerializers

# Create your views here.

class StudentMarksList(generics.ListCreateAPIView):
    queryset = StudentMarks.objects.all()
    serializer_class = StudentMarkSerializers



class StudentMarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentMarks.objects.all()
    serializer_class = StudentMarkSerializers
