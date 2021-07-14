from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name','weight','price','created_at','updated_at']
    list_filter = ['created_at',]
    list_editable = ['weight','price']
    ordering = ['-price',]