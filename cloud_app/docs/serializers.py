from rest_framework import serializers

from .models import Planet
from .models import Character
from .models import DataUpdate


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'



class DataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUpdate
        fields = '__all__'

