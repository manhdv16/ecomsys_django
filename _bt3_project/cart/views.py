from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from book.models import Book
from .models import CartItem
from .models import Cart
from django.contrib import messages
from decimal import Decimal  

import uuid
from django.utils import timezone
from django.db.models import Max


def _generate_cart_id():
    max_cart_id = Cart.objects.aggregate(Max('id'))['id__max']
    if max_cart_id is not None:
        cart_id = max_cart_id + 1
    else:
        cart_id = 1
    return cart_id

def addToCart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity', 1))

    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_id = _generate_cart_id()
        request.session['cart_id'] = cart_id

    cart, created = Cart.objects.get_or_create(session_key=cart_id)

    cart_item, created = CartItem.objects.get_or_create(    
        book_title=book.title,
        price=Decimal(book.price),
        cart=cart,
        img_url = book.cover_image,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return redirect('/cart/')

def view_cart(request):
    session_key = request.session.get('cart_id')
    cart_id = Cart.objects.get(session_key=session_key).id
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    total_price = sum(item.price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})