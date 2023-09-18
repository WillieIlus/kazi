from django.shortcuts import render

from .models import Country, County
from .serializers import CountrySerializer, CountySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CountryList(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'


class CountryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'


class CountyList(ListCreateAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    lookup_field = 'slug'


class CountyDetail(RetrieveUpdateDestroyAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    lookup_field = 'slug'


