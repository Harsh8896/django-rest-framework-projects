from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["id", "text", "author"]


    def validate_text(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Quote kam se kam 5 characters ka ho.")
        return value.strip()
