from django.shortcuts import render
from rest_framework import generics
from .models import Habit, Checkin
from .serializers import HabitSerializer, CheckinsSerializer

# Create your views here.

class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class CheckinsList(generics.ListCreateAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinsSerializer