from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Cars, OrderItem, Order
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


def add_to_cart_view(request, pk):
    cars = get_object_or_404(Cars, pk=pk)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(pk), {'quantity': 0, 'name': cars.name, 'price': cars.price})
    cart_item['quantity'] += 1
    cart[str(pk)] = cart_item
    request.session['cart'] = cart
    return redirect('index')


def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart_view(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart')


def clear_cart_view(request):
    request.session['cart'] = {}
    return redirect('cart')


def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    order = Order.objects.create()
    for pk, item in cart.items():
        cars = get_object_or_404(Cars, pk=pk)
        order_item = OrderItem.objects.create(cars=cars, quantity=item['quantity'])   
        order.items.add(order_item)

    order.save()
    request.session['cart'] = {}
    return render(request, 'checkout_success.html', {'order': order})


def order_history_view(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders}) 
 