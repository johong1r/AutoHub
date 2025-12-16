
from .forms import CarsForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from autohub.models import Cars


class CarsDeleteView(LoginRequiredMixin, DeleteView):
    model = Cars 
    template_name = 'custom_admin/delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CarsUpdateView(LoginRequiredMixin, UpdateView):
    model= Cars
    template_name = 'custom_admin/update.html'
    form_class = CarsForm
    context_object_name = 'cars'
    success_url = "/"

    def form_valid(self, form):
        form
        return super().form_valid(form)
    


class CarsCreateView(LoginRequiredMixin, CreateView):
    model = Cars
    template_name = 'custom_admin/create.html'
    form_class = CarsForm
    success_url = "/"

    def form_valid(self, form):
        form
        return super().form_valid(form)