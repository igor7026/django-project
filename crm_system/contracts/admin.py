from django.contrib import admin

from .models import Contract

# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "cost")
    fields = ("name", "start_date", "end_date", "product", "cost", "document")
