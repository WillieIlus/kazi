from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    search_fields = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('parent',)
    ordering = ('name',)
    list_filter = ('parent',)


admin.site.register(Category, CategoryAdmin)

