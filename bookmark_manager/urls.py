from django.urls import path, include
from .views import BookMarkViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("bookmarks", BookMarkViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]
