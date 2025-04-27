from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from products.models import Product
import json


def get_cart(request):
    '''
    Retrieve the cart from session or create a new one
    '''
    return request.session.setdefault('cart', [])


def RedirectHomeView(request):
    '''
    Redirect URL from '/' to '/home/'
    '''
    return redirect('home')


class HomeView(ListView):
    '''
    Renders home page with all the products and the cart
    '''
    template_name = 'home.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)
        return context


@require_POST
def add_to_cart(request):
    '''
    Adds an item to the cart stored in session
    Accepts both JSON and HTML form submissions
    '''
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        data = request.POST

    required_fields = {'id', 'name', 'quantity'}
    if not required_fields.issubset(data):
        return JsonResponse({'error': 'Missing fields'}, status=400)

    try:
        cart = get_cart(request)
        cart.append({
            'id': int(data['id']),
            'name': data['name'],
            'quantity': int(data['quantity']),
        })
        request.session.modified = True
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    if request.content_type != 'application/json':
        return redirect('home')

    return JsonResponse({'message': 'Item added to cart', 'cart': cart})
