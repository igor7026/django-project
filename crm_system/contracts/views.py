from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contract

# Create your views here.

class ContractsListView(ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'



class ContractsDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
 

class ContractsCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contracts-create.html'
    fields = ['name', 'start_date', 'end_date', 'product', 'cost']
    success_url = reverse_lazy('contracts:contracts-list')


class ContractsUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    fields = ['name', 'start_date', 'end_date', 'product', 'cost']
    success_url = reverse_lazy('contracts:contracts-list')


class ContractsDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts-list')
    
    

