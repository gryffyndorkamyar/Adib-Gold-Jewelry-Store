from django.shortcuts import redirect, render , get_object_or_404

from cart.cart import Cart
from shop.models import Product
from .forms import AddToCartForm
# Create your views here.
def cart_deatil(request):
    cart = Cart(request)
    return render(request,"cart/cart_detail.html",{'cart':cart})


def add_to_cart_view(request,product_id):
    cart = Cart(request)

    product = get_object_or_404(Product , id=product_id)
    form = AddToCartForm(data=request.POST)

    if form.is_valid():
        cd_data = form.cleaned_data
        quantity = cd_data['quantity'] 
        cart.add(product,quantity)
    
    return redirect("cart:cart_detail")


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product ,id=product_id)

    cart.remove(product)

    return redirect("cart:cart_detail")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")
        