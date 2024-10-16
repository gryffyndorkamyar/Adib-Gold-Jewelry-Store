from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.views import generic
from cart.cart import Cart
from .models import Order, OrderItem
from django.contrib import messages
# Create your views here.

@login_required
def create_order(request):
    
    cart = Cart(request)
    

    if len(cart) == 0:
        return redirect("shop:home")

    if request.method == "POST":
        order_form = OrderForm(request.POST) 
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user 
            order_obj.save()
        

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,product=product,
                    quantity = item['quantity'],
                    new_price = product.new_price,
                )

            cart.clear()
            



            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            
            request.session['order_id'] = order_obj.id 
            return redirect("orders:order_list")

    else:
        order_form = OrderForm()
        
    context = {
        'form': order_form
    }
    return render(request,"orders/order_create.html",context)


class OrdersListView(generic.ListView):
    model = Order 
    template_name = "orders/order_list.html"
    context_object_name = "orders"    

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items__product").order_by("-created")