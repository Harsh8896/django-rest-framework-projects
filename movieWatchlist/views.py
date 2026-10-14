from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics

# Create your views here.

class MovieWatchList(generics.ListCreateAPIView):
    queryset = Movie.objects.order_by("watched", "title")
    serializer_class = MovieSerializer


class MovieWatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer