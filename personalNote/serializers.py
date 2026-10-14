from rest_framework import serializers
from .models import PersonalNote


class PersonalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ["id", "title", "body", "pinned", "updated_at"]
        read_only_fields = ["updated_at"]