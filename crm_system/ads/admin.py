from django.contrib import admin

from .models import Ads

# Register your models here.

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget')
    fields = ('name', 'budget', 'product', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
