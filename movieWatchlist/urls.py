from django.urls import path
from .views import MovieWatchList, MovieWatchDetail


urlpatterns = [
    path("api/movie/", MovieWatchList.as_view()),
    path("api/movie/<int:pk>/", MovieWatchDetail.as_view()),

]
