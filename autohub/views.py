from django.shortcuts import render
from django.db.models import Q
from .models import Cars

def home_view(request):
    search_query = request.GET.get('search', '') 
    if search_query:
        cars = Cars.objects.filter(
            Q(name__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(brand__name__icontains=search_query)
        )
    else:
        cars = Cars.objects.all()  
    
    return render(request, 'homepage.html', {'cars': cars,
        'search': search_query})
    
    


