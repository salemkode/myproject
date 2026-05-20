from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = ['delivery_address']
    success_url = "/orders/"

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)
