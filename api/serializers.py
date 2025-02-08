from rest_framework import serializers
from .models import Audio, FIR


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class FIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIR
        fields = '__all__'
