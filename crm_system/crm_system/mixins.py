from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        # Добавляем сообщение об ошибке
        messages.error(self.request, "У вас нет прав доступа")
        # Перенаправляем на начальную страницу (измените 'index' на имя вашего URL)
        return redirect(
            reverse("index")
        )  # 'index' - это имя URL вашей начальной страницы
