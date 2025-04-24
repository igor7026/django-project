from django.contrib import admin

from .models import Lead

# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    fields = ('first_name', 'last_name', 'email', 'phone', 'ads', 'created_at')
    readonly_fields = ('created_at',)
