from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response


from rest_framework import generics

from rest_framework import viewsets

# Create your views here.

# @api_view(["GET", "POST"])
# def book_list(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Generic API creation 

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer