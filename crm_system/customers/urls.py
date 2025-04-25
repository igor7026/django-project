from django.urls import path

from customers.views import (
    CustomersListView,
    CustomersDetailView,
    CustomersCreateView,
    CustomersUpdateView,
    CustomersDeleteView,
)

app_name = 'customers'

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers-list'),
    path('<int:pk>', CustomersDetailView.as_view(), name='customers-detail'),
    path('new/', CustomersCreateView.as_view(), name='customers-create'),
    path('<int:pk>/edit/', CustomersUpdateView.as_view(), name='customers-update'),
    path('<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers-delete'),
]
    