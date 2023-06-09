from django.contrib import admin
from .models import Product

#model admin for showing products in admin panel 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',) }

# Register your models here.
admin.site.register(Product, ProductAdmin)
