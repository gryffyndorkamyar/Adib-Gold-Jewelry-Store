from . import views
from django.urls import path

app_name = "cart"

urlpatterns = [
    path("detail/",views.cart_deatil,name="cart_detail"),
    path("add/<int:product_id>/", views.add_to_cart_view, name="cart_add"),
    path("remove/<int:product_id>/", views.remove_cart, name="cart_remove"),
    path("clear/", views.clear_cart, name="cart_clear")
]
