from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path("", views.product_index_list, name="home"),
    path("products/<slug:category_slug>/", views.product_index_list, name="products_by_category"),
    path("product_detail/<int:id>/<slug:slug>/" , views.product_detail,name="product_detail"),
    path("about_us/", views.about_us, name="about_us")


]
