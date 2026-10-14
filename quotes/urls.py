from django.urls import path, include
from .views import QuoteViewSet, random_quote
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("quotes", QuoteViewSet)

urlpatterns = [
    path("api/random-quote/", random_quote),
    path("api/", include(router.urls)),
]
