from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Leads


class LeadsListView(ListView):
    model = Leads
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadsDetailView(DetailView):
    model = Leads
    template_name = 'leads/leads-detail.html'


class LeadsCreateView(CreateView):
    model = Leads
    fields = ['first_name', 'last_name', 'email', 'phone', 'ads']
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadsUpdateView(UpdateView):
    model = Leads
    fields = ['first_name', 'last_name', 'email', 'phone', 'ads']
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadsDeleteView(DeleteView):
    model = Leads
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads-list')
    


