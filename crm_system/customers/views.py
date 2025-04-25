from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from crm_system.mixins import CustomPermissionRequiredMixin
from .models import Customer

# Create your views here.

class CustomersListView(CustomPermissionRequiredMixin, ListView):
    permission_required = 'customers.view_customer'
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomersDetailView(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'customers.view_customer'
    model = Customer
    template_name = 'customers/customers-detail.html'


class CustomersCreateView(CustomPermissionRequiredMixin, CreateView):
    permission_required = 'customers.add_customer'
    model = Customer
    template_name = 'customers/customers-create.html'
    fields = ['lead', 'contract']
    success_url = reverse_lazy('customers:customers-list')


class CustomersUpdateView(CustomPermissionRequiredMixin, UpdateView):
    permission_required = 'customers.change_customer'
    model = Customer
    template_name = 'customers/customers-edit.html'
    fields = ['lead', 'contract']
    success_url = reverse_lazy('customers:customers-list')


class CustomersDeleteView(CustomPermissionRequiredMixin, DeleteView):
    permission_required = 'customers.delete_customer'
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers-list')

