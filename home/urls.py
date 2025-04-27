from django.urls import path
from .views import HomeView, RedirectHomeView, add_to_cart

urlpatterns = [
    path('', RedirectHomeView, name='redirect_home'),
    path('home/', HomeView.as_view(), name='home'),
    path('cart/add', add_to_cart, name='add_to_cart'),
]
