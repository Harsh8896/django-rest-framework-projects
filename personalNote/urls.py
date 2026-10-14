from .views import PersonalNoteList, PersonalNoteDetail
from django.urls import path

urlpatterns = [
    path("api/personalnote", PersonalNoteList.as_view()),
    path("api/personalnote/<int:pk>/", PersonalNoteDetail.as_view()),
]
