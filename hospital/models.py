from django.db import models

# Create your models here.

class PateintModal(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    