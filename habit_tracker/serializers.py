from rest_framework import serializers
from .models import Habit, Checkin

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "name", "target_per_week"]


class CheckinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ["id", "habit_name", "date"]

        def validate_habit_name(self, value):
            if not Habit.objects.filter(name = value).exists():
                raise serializers.ValidationError("Is naam ki koi habit nahi hai. Pehle habit banao.")
            return value