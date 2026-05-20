from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from delivery.models import Deliverer


class DelivererListView(LoginRequiredMixin, ListView):
    model = Deliverer
    template_name = 'delivery/deliverer_list.html'
    context_object_name = 'deliverers'


class DelivererDetailView(LoginRequiredMixin, DetailView):
    model = Deliverer
    template_name = 'delivery/deliverer_detail.html'
    context_object_name = 'deliverer'


class DelivererCreateView(LoginRequiredMixin, CreateView):
    model = Deliverer
    template_name = 'delivery/deliverer_form.html'
    fields = ['name', 'phone_number', 'is_available']
    success_url = "/deliverers/"


class DelivererUpdateView(LoginRequiredMixin, UpdateView):
    model = Deliverer
    template_name = 'delivery/deliverer_form.html'
    fields = ['name', 'phone_number', 'is_available']
    success_url = "/deliverers/"


class DelivererDeleteView(LoginRequiredMixin, DeleteView):
    model = Deliverer
    template_name = 'delivery/deliverer_confirm_delete.html'
    success_url = "/deliverers/"
