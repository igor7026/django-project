from django.contrib import admin

from .models import Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "cost"]
    readonly_fields = ["created_at", "updated_at"]  # делает поля только для чтения
    fields = [
        "name",
        "description",
        "cost",
        "created_at",
        "updated_at",
    ]  # порядок полей в форме редактирования
