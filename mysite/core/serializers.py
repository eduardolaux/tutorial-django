from .models import Person, Place
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):

  class Meta:
      model = Place
      fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
  places = PlaceSerializer(many=True, read_only=True)

  class Meta:
      model = Person
      fields = '__all__'