from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "year", "gener", "watched", "rating"]


# validate() ka kaam hai check karna ki user ne jo data bheja hai, woh tumhare business rules ke according sahi hai ya nahi.
# Yahan problem kya hai?
# - watched = false — movie dekhi hi nahi.
# - rating = 5 — phir bhi 5 star de diye.
# Ab tumhe is galat data ko database mein save hone se rokna hai. Yahi kaam tumhara validate() karega.
    def validate(self, data):

# Matlab: DRF user ke data ko check karne ke liye is method ko call karta hai.
# - self = current serializer object.
# - data = request se aaya hua data, jo field-level validation se pass ho chuka hai.

        watched = data.get("watched", getattr(self.instance, "watched", False))


# Is line ka matlab hai: pehle request mein watched dekho. Agar nahi mila, toh existing movie ki value dekho. Agar existing movie bhi nahi hai, toh default False lo.
# Example:
# Situation	watched ki value
# Request mein True hai	True
# Request mein False hai	False
# PATCH mein field missing hai, existing movie watched hai	True
# Nayi movie hai aur field missing hai	False
# getattr(self.instance, "watched", False) existing object se value leta hai. Agar object nahi hai ya attribute nahi milta, toh False use hota hai.

        rating = data.get("rating")
        if rating is not None and not watched:
            raise serializers.ValidationError("Rating sirf dekhi hui movie ko de sakte ho.")
        return data
