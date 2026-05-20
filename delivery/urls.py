from django.urls import path

from .views import (
    DelivererCreateView,
    DelivererDeleteView,
    DelivererDetailView,
    DelivererListView,
    DelivererUpdateView,
)

urlpatterns = [
    path('', DelivererListView.as_view(), name='deliverer-list'),
    path('create/', DelivererCreateView.as_view(), name='deliverer-create'),
    path('<int:pk>/', DelivererDetailView.as_view(), name='deliverer-detail'),
    path('<int:pk>/update/', DelivererUpdateView.as_view(), name='deliverer-update'),
    path('<int:pk>/delete/', DelivererDeleteView.as_view(), name='deliverer-delete'),
]
