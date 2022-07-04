from .models import *


def categories(request):
    all_category = Category.objects.all()
    all_tag = Tag.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'all_category': all_category, 'all_tag': all_tag, 'items': items, 'order': order, 'cartItems': cartItems}
    return context


