from django.shortcuts import render, get_object_or_404
from .models import *

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

def cart_detail(request):
    cart = Cart.objects.first()
    cart_items = cart.cartitem_set.all() if cart else []
    return render(request, 'catalog/cart_detail.html', {'cart_items': cart_items})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(pk=cart_id).first()

    if not cart:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()


