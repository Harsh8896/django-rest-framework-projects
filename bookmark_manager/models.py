from django.db import models

# Create your models here.

class BookMarkManager(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    