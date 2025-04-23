from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ads

# Create your views here.

class AdsListView(ListView):
    model = Ads
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'

class AdsDetailView(DetailView):
    model = Ads
    template_name = 'ads/ads-detail.html'
    

class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads-list')

class AdsUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ads-list')

class AdsDeleteView(DeleteView):
    model = Ads
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads-list')


class AdsStatisticView(ListView):
    model = Ads
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Ads.objects.all()
    
    
