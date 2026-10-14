from rest_framework import serializers
from . models import StreamPlatForm, WatchList


# etni chije frontend se aayengo hme apne backend me store kr lena hai ye sari chije frontend se aayengi

class WatchListSerializers(serializers.ModelSerializer):
    class Meta:
         model = WatchList
         fields = "__all__"




class StreamPlatFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatForm
        fields = "__all__"
