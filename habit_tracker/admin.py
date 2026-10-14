from django.contrib import admin
from .models import Habit, Checkin

# Register your models here.

admin.site.register(Habit)
admin.site.register(Checkin)