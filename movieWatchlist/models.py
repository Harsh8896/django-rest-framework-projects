from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    GENER_CHOICE = [
        ("action", "Action"),
        ("comedy", "Comedy"),
        ("drama", "Drama"),
        ("horror", "Horror"),
        ("romance", "Romance"),
        ("thriller", "thriller")
    ]

    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    gener = models.CharField(max_length=20, choices=GENER_CHOICE)
    watched = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.title} - {self.year}"
    