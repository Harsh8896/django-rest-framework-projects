from django.shortcuts import render
from rest_framework import viewsets
from .models import BookMarkManager
from .serializers import BookMarkSerializer

# Create your views here.

class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMarkManager.objects.all()
    serializer_class = BookMarkSerializer