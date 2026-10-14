from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import StreamPlatForm, WatchList
from .serializers import WatchListSerializers, StreamPlatFormSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404



from rest_framework import mixins
from rest_framework import generics




# Create your views here.

# @api_view(["GET", "POST"])

# def movie_list(request):
#     if request.method == "GET":
#         movie_list = WatchList.objects.all()
#         serialized = WatchListSerializers(movie_list, many=True)
#         return Response(serialized.data)

#     elif request.method == "POST":
#         serialized = WatchListSerializers(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, pk):
#     try:
#         movie = WatchList.objects.get(pk=pk)
#     except WatchList.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serialized = WatchListSerializers(movie)
#         return Response(serialized.data)

#     elif request.method == "PUT":
#         serialized = WatchListSerializers(movie, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)








# class StreamPlatFormList(APIView):

#     def get(self, request, format=None):
#         movie_list = WatchList.objects.all()
#         serializer = WatchListSerializers(movie_list, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = WatchListSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )






# class StreamPlatFormDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serialized = WatchListSerializers(movie)
#         return Response(serialized.data)

#     def put(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serialized = WatchListSerializers(
#             movie,
#             data=request.data
#         )

#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)

#         return Response(
#             serialized.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )









# class StreamPlatFormList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = StreamPlatForm.objects.all()
#     serializer_class = StreamPlatFormSerializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class StreamPlatFormDetail(mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
#     ):

#     queryset = StreamPlatForm.objects.all()
#     serializer_class = StreamPlatFormSerializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)






















class StreamPlatFormList(generics.ListCreateAPIView):
      queryset = StreamPlatForm.objects.all()
      serializer_class = StreamPlatFormSerializers



class StreamPlatFormDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = StreamPlatForm.objects.all()
      serializer_class = StreamPlatFormSerializers










      