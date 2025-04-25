from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Ads

# Create your views here.

class AdsListView(PermissionRequiredMixin, ListView):
    permission_required = 'ads.view_ads'
    model = Ads
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'

class AdsDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'ads.view_ads'
    model = Ads
    template_name = 'ads/ads-detail.html'
    

class AdsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'ads.add_ads'
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads-list')

class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'ads.change_ads'
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ads-list')

class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'ads.delete_ads'
    model = Ads
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads-list')


class AdsStatisticView(PermissionRequiredMixin, ListView):
    permission_required = 'ads.view_ads'
    model = Ads
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Ads.objects.all()
    
    
