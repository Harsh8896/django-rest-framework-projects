from rest_framework import serializers
from .models import BookMarkManager


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMarkManager
        fields = ["id", "title", "url", "note","created_at"]
        read_only_fields = ["created_at"]