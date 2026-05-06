"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, DeleteCustomer

urlpatterns = [
    path('', CustomerCreateView.as_view(), name='customer-create'),
    path('list/', CustomerListView.as_view(), name='customer-list'),
    path('list/details/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('list/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-detail'),
    path('list/delete/<int:pk>/', DeleteCustomer.as_view(), name='customer-detail'),
]
    
