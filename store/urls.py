from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('products', views.products, name='products'),
    path('product-view/<int:pk>', views.product_view, name='product-view'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('update_item', views.updateItem, name='update_item'),
]