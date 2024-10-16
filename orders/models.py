from django.db import models
from Adib import settings
from shop.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="orders",verbose_name="کاربر")
    first_name = models.CharField(max_length=100,verbose_name="نام")
    last_name = models.CharField(max_length=100,verbose_name="نام خانوادگی")
    phone_number = models.CharField(max_length=11,verbose_name="شماره تلفن")
    address = models.TextField(verbose_name="آدرس")

    order_notes = models.TextField(blank=True, null=True,verbose_name="یادداشت سفارش")

    zarinpal_authority = models.CharField(max_length=255,blank=True)
    zarinpal_ref_id = models.CharField(max_length=200, blank=True)
    zarinpal_data = models.TextField(blank=True)

    is_paid = models.BooleanField(default=False ,verbose_name="وضعیت پرداخت")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True,verbose_name="تاریخ به روز رسانی")

    def __str__(self) -> str:
        return self.phone_number
    
    def get_total_price_pay(self):
        return sum(item.quantity * item.new_price for item in self.items.all())

    class Meta:
        verbose_name="سفارش"
        verbose_name_plural ="سفارش ها"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items",verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items",verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1,verbose_name="تعداد")
    new_price = models.PositiveBigIntegerField(verbose_name="قیمت نهایی")

    


    def __str__(self) -> str:
        return self.product.title
