from django.urls import path

from products.views import (
    ProductsListView,
    ProductsDetailView,
    ProductsCreateView,
    ProductsUpdateView,
    ProductsDeleteView,
)

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-list"),
    path("<int:pk>", ProductsDetailView.as_view(), name="products-detail"),
    path("new/", ProductsCreateView.as_view(), name="products-create"),
    path("<int:pk>/edit/", ProductsUpdateView.as_view(), name="products-update"),
    path("<int:pk>/delete/", ProductsDeleteView.as_view(), name="products-delete"),
]
