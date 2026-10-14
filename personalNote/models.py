from django.db import models

# Create your models here.

class PersonalNote(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    pinned = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    