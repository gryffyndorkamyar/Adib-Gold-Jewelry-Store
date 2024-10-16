from . import views
from django.urls import path
app_name = "orders"
urlpatterns = [
    path("create/", views.create_order, name="order_create"),
    path("list/",views.OrdersListView.as_view(),name="order_list")
    
]
