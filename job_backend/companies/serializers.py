from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    logo_url = serializers.CharField(source='get_logo_url', read_only=True)
    county = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'description', 'county', 'user', 'url', 'logo_url', 'address', 'phone', 'email', 'website', 'logo', 'cover')
        read_only_fields = ('slug', 'url', 'logo_url', 'user', 'county')



