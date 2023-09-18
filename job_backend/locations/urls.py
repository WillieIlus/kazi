from django.urls import path

from .views import CountryList, CountryDetail, CountyList, CountyDetail

app_name = 'locations'

urlpatterns = [
    path('countries/', CountryList.as_view(), name='country_list'),
    path('countries/<slug:slug>/', CountryDetail.as_view(), name='country_detail'),
    path('counties/', CountyList.as_view(), name='county_list'),
    path('counties/<slug:slug>/', CountyDetail.as_view(), name='county_detail'),
]
