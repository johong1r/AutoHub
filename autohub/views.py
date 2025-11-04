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

        cars = Cars.objects.all()

        model = self.request.GET.get('model')
        location = self.request.GET.get('location')
        country = self.request.GET.get('country')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        year = self.request.GET.get('year')

        if model:
            cars = cars.filter(model__icontains=model)
        if location:
            cars = cars.filter(location__icontains=location)
        if country:
            cars = cars.filter(country__icontains=country)
        if min_price:
            cars = cars.filter(price__gte=min_price)
        if max_price:
            cars = cars.filter(price__lte=max_price)
        if year:
            cars = cars.filter(year=year)

        years = Cars.objects.values_list('year', flat=True).distinct().order_by('-year')

        context['cars'] = cars
        context['years'] = years
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
    
    


