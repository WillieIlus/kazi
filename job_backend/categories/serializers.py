from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'parent', 'url')
        read_only_fields = ('slug', 'url')
