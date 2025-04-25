from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from crm_system.mixins import CustomPermissionRequiredMixin
from .models import Contract

# Create your views here.

class ContractsListView(CustomPermissionRequiredMixin, ListView):
    permission_required = 'contracts.view_contract'
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'



class ContractsDetailView(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'contracts.view_contract'
    model = Contract
    template_name = 'contracts/contracts-detail.html'
 

class ContractsCreateView(CustomPermissionRequiredMixin, CreateView):
    permission_required = 'contracts.add_contract'
    model = Contract
    template_name = 'contracts/contracts-create.html'
    fields = ['name', 'start_date', 'end_date', 'product', 'cost', 'document']
    success_url = reverse_lazy('contracts:contracts-list')


class ContractsUpdateView(CustomPermissionRequiredMixin, UpdateView):
    permission_required = 'contracts.change_contract'
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    fields = ['name', 'start_date', 'end_date', 'product', 'cost', 'document']
    success_url = reverse_lazy('contracts:contracts-list')


class ContractsDeleteView(CustomPermissionRequiredMixin, DeleteView):
    permission_required = 'contracts.delete_contract'
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts-list')
    
    

