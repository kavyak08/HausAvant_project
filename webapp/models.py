from django.db import models

# Create your models here.

class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=300,null=True,blank=True)

class SignupDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Rpassword = models.CharField(max_length=100,null=True,blank=True)


class CartDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_price = models.IntegerField(null=True,blank=True)
    Product_name = models.CharField(max_length=100,null=True,blank=True)


class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.TextField(max_length=100,null=True,blank=True)
    Postal = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.TextField(max_length=100,null=True,blank=True)
    Total_price = models.IntegerField(null=True,blank=True)
