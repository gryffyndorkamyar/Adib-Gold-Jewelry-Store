from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.Image
    extra = 0

class ProductFeatureInline(admin.TabularInline):
    model = models.ProductFeature
    extra = 0

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","inventory","new_price","created","updated"]
    inlines = [ProductFeatureInline,ImageInline]

