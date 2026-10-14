from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "cook_minutes", "is_veg"]
    list_filter = ["is_veg"]
    search_fields = ["name"]