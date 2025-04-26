from django.urls import path

from ads.views import (
    AdsListView,
    AdsDetailView,
    AdsCreateView,
    AdsUpdateView,
    AdsDeleteView,
    AdsStatisticView,
)

app_name = "ads"

urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    path("<int:pk>", AdsDetailView.as_view(), name="ads-detail"),
    path("new/", AdsCreateView.as_view(), name="ads-create"),
    path("<int:pk>/edit/", AdsUpdateView.as_view(), name="ads-update"),
    path("<int:pk>/delete/", AdsDeleteView.as_view(), name="ads-delete"),
    path("statistic/", AdsStatisticView.as_view(), name="ads-statistic"),
]
