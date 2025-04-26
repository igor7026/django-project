from django.urls import path

from leads.views import (
    LeadsListView,
    LeadsDetailView,
    LeadsCreateView,
    LeadsUpdateView,
    LeadsDeleteView,
)

app_name = "leads"

urlpatterns = [
    path("", LeadsListView.as_view(), name="leads-list"),
    path("<int:pk>", LeadsDetailView.as_view(), name="leads-detail"),
    path("new/", LeadsCreateView.as_view(), name="leads-create"),
    path("<int:pk>/edit/", LeadsUpdateView.as_view(), name="leads-update"),
    path("<int:pk>/delete/", LeadsDeleteView.as_view(), name="leads-delete"),
]
