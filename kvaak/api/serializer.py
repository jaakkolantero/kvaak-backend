from rest_framework import serializers
from .models import Species
from .models import Sighting


# Serializers define the API representation.
class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'name',)


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = ('id', 'date_time', 'description', 'species', 'count',)
