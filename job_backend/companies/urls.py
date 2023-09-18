from django.urls import path

from .views import CompanyList, CompanyDetail, CompanyListUser

app_name = 'companies'

urlpatterns = [
    path('', CompanyList.as_view(), name='company_list'),
    path('my/', CompanyListUser.as_view(), name='company_list_user'),
    path('<slug:slug>/', CompanyDetail.as_view(), name='company_detail'),

]
