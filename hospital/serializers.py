from rest_framework import serializers
from .models import PateintModal


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PateintModal
        fields = "__all__"
        read_only = ["id", "created_at"]