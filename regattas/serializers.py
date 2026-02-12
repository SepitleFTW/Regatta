#serializer to convert data to json format

from rest_framework import serializers
from .models import Club, Regatta, Race, Result

"""
Creating modelSeri for each of my 4 models
"""
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model= Club
        fields = '__all__'

class RegattaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Regatta
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'