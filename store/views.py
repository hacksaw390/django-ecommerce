from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
# Create your views here.


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products': products,'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']



    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def product_view(request, pk):
    product = Product.objects.prefetch_related('color').prefetch_related('size').get(id=pk)
    context = {'product': product}
    return render(request, 'store/product-view.html', context)


def updateItem(request):
    print('ok')
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    print(productId)
    print(action)
    return JsonResponse('Item was added...', safe=False)


def orderProsess(request):
    transection_id = datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:

        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transection_id = transection_id

    print(transection_id)

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    print(order.transection_id)

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )



    return JsonResponse('ok', safe=False)
