from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'county', 'user')
    search_fields = ('name', 'slug', 'county', 'user')
    prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ('user',)
    ordering = ('name',)
    list_filter = ('county',)

admin.site.register(Company, CompanyAdmin)