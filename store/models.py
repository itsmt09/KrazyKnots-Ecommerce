from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

# model for storing product info
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    # brand name or Artisan's name can be filled here
    brand_name   = models.CharField(max_length=50)
    description  = models.TextField(max_length=500, blank=True)
    price        = models.IntegerField()
    slug         = models.SlugField(max_length=200, unique=True)
    stock        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products', height_field=None, width_field=None, max_length=None)
    is_available = models.BooleanField(default=True)
    # foreign key for category model
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug])
    
variation_category_choices = (
    ('color', 'color'),
    # for some products we can add size option in future that's why choices are made
        )

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    variation_category = models.CharField(max_length=100, choices= variation_category_choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.variation_value)  # self.product
    