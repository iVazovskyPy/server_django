from django.contrib import admin
from .models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_name = ('name', 'unit_type', 'parent')
    list_filter = ('unit_type',)
    search_field = ('name', 'parent__name')
