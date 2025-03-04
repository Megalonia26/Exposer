from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CatgoryModel(admin.ModelAdmin):
    list_display = ["id", "name", "img"]

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category", "discount", "img", "still_available"]