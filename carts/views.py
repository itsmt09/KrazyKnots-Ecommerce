from django.http import HttpResponse
from django.shortcuts import redirect, render

from carts.models import Cart, CartItem
from store.models import Product

# Create your views here.

def _cart_id(request):
    cart = request.session._get_or_create_session_key()
    # if not request.session.session_key:
    #     request.session.save()
    # cart = request.session.session_key
    # if not cart:
    #     cart = request._session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    # return HttpResponse()
    # exit()
    return redirect('cart')

def decrease_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = Product.objects.get(id = product_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = Product.objects.get(id = product_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    cart_item.delete()
    return redirect('cart')


def cart(request, total_price=0, total_quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        for cart_item in cart_items:
            total_price += (cart_item.product.price * cart_item.quantity)
            total_quantity += cart_item.quantity
        
    except:
        pass

    context = {
        'total_price': total_price,
        'total_quantity': total_quantity,
        'cart_items': cart_items,
    }

    return render(request, 'store/cart.html', context)