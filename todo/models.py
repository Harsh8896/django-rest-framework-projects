from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    