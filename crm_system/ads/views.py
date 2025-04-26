from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.db.models import Q


from crm_system.mixins import CustomPermissionRequiredMixin
from .models import Ads

# Create your views here.


class AdsListView(CustomPermissionRequiredMixin, ListView):
    permission_required = "ads.view_ads"
    model = Ads
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsDetailView(CustomPermissionRequiredMixin, DetailView):
    permission_required = "ads.view_ads"
    model = Ads
    template_name = "ads/ads-detail.html"


class AdsCreateView(CustomPermissionRequiredMixin, CreateView):
    permission_required = "ads.add_ads"
    model = Ads
    fields = ["name", "budget", "product"]
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:ads-list")


class AdsUpdateView(CustomPermissionRequiredMixin, UpdateView):
    permission_required = "ads.change_ads"
    model = Ads
    fields = ["name", "budget", "product"]
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")


class AdsDeleteView(CustomPermissionRequiredMixin, DeleteView):
    permission_required = "ads.delete_ads"
    model = Ads
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:ads-list")


class AdsStatisticView(CustomPermissionRequiredMixin, ListView):
    permission_required = "ads.view_ads"
    model = Ads
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.annotate(
            leads_count=Count("lead"),
            customers_count=Count("lead__status", filter=Q(lead__status="customer")),
            profit=Sum("lead__customer__contract__cost") - Sum("budget"),
        )

        return queryset
