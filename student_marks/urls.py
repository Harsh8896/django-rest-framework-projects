from django.urls import path
from .views import StudentMarksList, StudentMarksDetail


urlpatterns = [
    path("api/student_marks/", StudentMarksList.as_view()),
    path("api/student_marks/<int:pk>/", StudentMarksDetail.as_view()),
]