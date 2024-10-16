from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    slug = models.SlugField()

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:products_by_category", args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products",verbose_name="دسته بندی")
    title = models.CharField(max_length=100,verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    inventory = models.BooleanField(default=True, verbose_name="موجودی")
    price = models.PositiveBigIntegerField(default=0,verbose_name="قیمت")
    off = models.PositiveIntegerField(default=0,verbose_name="تخفیف")
    new_price = models.PositiveBigIntegerField(default=0,verbose_name="قیمت بعد تخفیف")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True,verbose_name="تاریخ به روز رسانی")
    slug = models.SlugField()


    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id,self.slug])
    


    class Meta:
        ordering = ["-created"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]
    

    def __str__(self) -> str:
        return self.title
    
    

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="images")
    file = models.ImageField(upload_to="products_image",blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "عکس محصول"
        verbose_name_plural = "عکس محصولات"

class ProductFeature(models.Model):
    name = models.CharField(max_length=225,verbose_name="نام")
    value = models.CharField(max_length=225,verbose_name="مقدار")
    product = models.ForeignKey(Product,related_name="features",on_delete=models.CASCADE,verbose_name="محصول")

    def __str__(self) -> str:
        return f"{self.name} : {self.value}"
    
    class Meta:
        verbose_name = "ویژگی "
        verbose_name_plural = "ویژگی ها"