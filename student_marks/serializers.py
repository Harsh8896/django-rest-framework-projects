from rest_framework import serializers 
from .models import StudentMarks


class StudentMarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = ["id", "name", "roll_no", "math", "science", "english", "percentage"]