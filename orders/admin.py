from django.contrib import admin

from orders.models import OrderItem

from . import models

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1 

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","phone_number", "first_name","last_name","created","is_paid"]
    inlines = [OrderItemInline]

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "new_price"]
