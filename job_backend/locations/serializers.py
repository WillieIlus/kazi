from rest_framework import serializers
from .models import Country, County


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'slug', 'code', 'flag')


class CountySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = County
        fields = ('id', 'name', 'slug', 'country')
