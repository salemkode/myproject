from django.shortcuts import render
from .models import Customer
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

def home(request):
    return render(request, 'customers/index.html')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/index.html'
    fields = ['name', 'phone_number']
    success_url = "/customers/list"

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    fields = ['name', 'phone_number']
    success_url = "/customers/list"

class DeleteCustomer(DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    success_url = "/customers/list"