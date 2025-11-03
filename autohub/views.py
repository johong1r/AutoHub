from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Cars
from django.views.generic import TemplateView, DetailView


class CarsDetailView(DetailView):
    model = Cars
    template_name = 'detail.html'
    context_object_name = 'cars'


class HomeTemplateView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        if query:
            cars = Cars.objects.filter(name__icontains=query)
        else:
            cars = Cars.objects.all()
        context['cars'] = cars
        context['title'] = 'Главная страница'
        return context


# def home_view(request):
#     search_query = request.GET.get('search', '') 
#     if search_query:
#         cars = Cars.objects.filter(
#             Q(name__icontains=search_query) |
#             Q(model__icontains=search_query) |
#             Q(brand__name__icontains=search_query)
#         )
#     else:
#         cars = Cars.objects.all()  
    
#     return render(request, 'homepage.html', {'cars': cars,
#         'search': search_query})
    
    


