from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet

router = DefaultRouter()
router.register("recipes", RecipeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]