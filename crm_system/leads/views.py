from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from crm_system.mixins import CustomPermissionRequiredMixin
from .models import Lead


class LeadsListView(CustomPermissionRequiredMixin, ListView):
    permission_required = "leads.view_lead"
    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadsDetailView(CustomPermissionRequiredMixin, DetailView):
    permission_required = "leads.view_lead"
    model = Lead
    template_name = "leads/leads-detail.html"


class LeadsCreateView(CustomPermissionRequiredMixin, CreateView):
    permission_required = "leads.add_lead"
    model = Lead
    fields = ["first_name", "last_name", "email", "phone", "ads"]
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")


class LeadsUpdateView(CustomPermissionRequiredMixin, UpdateView):
    permission_required = "leads.change_lead"
    model = Lead
    fields = ["first_name", "last_name", "email", "phone", "ads"]
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("leads:leads-list")


class LeadsDeleteView(CustomPermissionRequiredMixin, DeleteView):
    permission_required = "leads.delete_lead"
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
