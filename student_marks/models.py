from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class StudentMarks(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20, unique=True)
    math = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    science = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    english = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["roll_no"]

    @property
    def percentage(self):
        total = self.math + self.science + self.english
        return round(total / 300 * 100, 2)

    def __str__(self):
        return self.name
    