from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from cart.forms import AddToCartForm
from django.db.models import Q 
# Create your views here.
def product_index_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    recent_products = Product.objects.all()[:3]

    query = request.GET.get("q")
    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        "category":category,
        "categories":categories,
        "products":products,
        "recent_products": recent_products,
        'query': query,
        
    }
    return render(request,"shop/index.html", context=context)

def product_detail(request,slug,id):
    product = get_object_or_404(Product, slug=slug, id=id) 
    context = {
            'product':product,
            'add_to_cart_form':AddToCartForm(),
        }
    
    return render(request,'shop/product_detail.html',context)

    
def about_us(request):
    return render(request, "shop/about_us.html")