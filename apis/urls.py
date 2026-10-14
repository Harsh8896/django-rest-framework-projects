from django.urls import path
from . import views

urlpatterns = [
    # path("list/", views.movie_list, name = "movie-list"),
    # path("list/<int:pk>/", views.movie_detail, name = "movie-detail")

    path("stream/", views.StreamPlatFormList.as_view(), name="stream_platform"),
    path("stream/<int:pk>/", views.StreamPlatFormDetail.as_view(), name="stream-detail")
]