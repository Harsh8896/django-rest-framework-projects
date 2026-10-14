from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    ingredients = models.TextField(help_text="Har line me ek ingredient")
    steps = models.TextField()
    cook_minutes = models.PositiveIntegerField()
    is_veg = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name