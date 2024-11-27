from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=300,null=True,blank=True)
    Image = models.ImageField(upload_to="category_images",null=True,blank=True)

class ProductDb(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    Product = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Manufacture = models.TextField(max_length=300, null=True, blank=True)
    Description = models.TextField(max_length=300, null=True, blank=True)
    Image1 = models.ImageField(upload_to="product_images",null=True,blank=True)
    Image2 = models.ImageField(upload_to="product_images",null=True,blank=True)
    Image3 = models.ImageField(upload_to="product_images",null=True,blank=True)




