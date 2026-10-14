from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    target_per_week = models.PositiveSmallIntegerField(default=7, validators=[MinValueValidator(1), MaxValueValidator(7)])

    def __str__(self):
        return self.name


class Checkin(models.Model):
    habit_name = models.CharField(max_length=100)
    date = models.DateField(default=date.today)

    ordering = ["-date"]


    def __str__(self):
        return f"{self.habit_name} {self.date}"
    