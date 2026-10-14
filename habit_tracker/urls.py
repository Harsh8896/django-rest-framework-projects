from django.urls import path
from .views import HabitList, HabitDetail, CheckinsList


urlpatterns = [
    path("api/habit_list/", HabitList.as_view()),
    path("api/habit_list/<int:pk>/", HabitDetail.as_view()),
    path("api/checkins/", CheckinsList.as_view()),

]
