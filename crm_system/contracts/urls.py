from django.urls import path

from contracts.views import (
    ContractsListView,
    ContractsDetailView,
    ContractsCreateView,
    ContractsUpdateView,
    ContractsDeleteView,
)

app_name = "contracts"

urlpatterns = [
    path("", ContractsListView.as_view(), name="contracts-list"),
    path("<int:pk>", ContractsDetailView.as_view(), name="contracts-detail"),
    path("new/", ContractsCreateView.as_view(), name="contracts-create"),
    path("<int:pk>/edit/", ContractsUpdateView.as_view(), name="contracts-update"),
    path("<int:pk>/delete/", ContractsDeleteView.as_view(), name="contracts-delete"),
]
