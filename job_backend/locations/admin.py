from django.contrib import admin

from .models import Country, County


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'code', 'flag')
    list_filter = ('name', 'code')
    search_fields = ('name', 'code')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'country')
    list_filter = ('name', 'country')
    search_fields = ('name', 'country')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


admin.site.register(Country, CountryAdmin)
admin.site.register(County, CountyAdmin)

