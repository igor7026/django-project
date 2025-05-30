from django.views.generic import TemplateView
from products.models import Product
from ads.models import Ads
from leads.models import Lead
from customers.models import Customer


class DashboardView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем количество объектов для каждой модели
        context["products_count"] = Product.objects.count()
        context["ads_count"] = Ads.objects.count()
        context["leads_count"] = Lead.objects.count()
        context["customers_count"] = Customer.objects.count()

        return context
