from django.shortcuts import render
from .models import PersonalNote
from .serializers import PersonalNoteSerializer
from rest_framework import generics


# Create your views here.

class PersonalNoteList(generics.ListCreateAPIView):
    queryset = PersonalNote.objects.order_by("-pinned", "updated_at")
    serializer_class = PersonalNoteSerializer


class PersonalNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalNote.objects.all()
    serializer_class = PersonalNoteSerializer
