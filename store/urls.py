from django.contrib import admin
from django.urls import include, path

from products.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('deliverers/', include('delivery.urls')),
    path('orders/', include('orders.urls')),
    path('api/', include('api.urls')),
    path('auth/', include('auth.urls')),
]
