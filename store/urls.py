from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product-view', views.product_view, name='product-view'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]