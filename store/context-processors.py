import json

from .models import *


def categories(request):
    all_category = Category.objects.all()
    all_tag = Tag.objects.all()
#
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         try:
#             cart = json.loads(request.COOKIES['cart'])
#         except:
#             cart = {}
#
#         print(cart)
#         items = []
#         order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
#         cartItems = order['get_cart_items']
#
#         for i in cart:
#             cartItems += cart[i]['quantity']
#
#             product = Product.objects.get(id=i)
#             total = (product.price * cart[i]['quantity'])
#
#             order['get_cart_total'] += total
#             order['get_cart_items'] += cart[i]['quantity']
#
#             item = {
#                 'product': {
#                     'id':product.id,
#                     'name':product.name,
#                     'price':product.price,
#                     # 'all_image':product.all_image,
#                     },
#                 'quantity': cart[i]['quantity'],
#                 'get_total': total
#                 }
#             items.append(item)
    context = {'all_category': all_category, 'all_tag': all_tag}
    return context


