from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from customers.models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    fields = ['name', 'phone_number']
    success_url = "/customers/"


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    fields = ['name', 'phone_number']
    success_url = "/customers/"


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = "/customers/"
