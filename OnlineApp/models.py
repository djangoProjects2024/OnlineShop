from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user    =   models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name    =   models.CharField(max_length=100,null=True)
    email   =   models.EmailField()
    def __str__(self):
        return self.name
class Product(models.Model):
    name    =   models.CharField(max_length=100,null=True)
    price   =   models.FloatField()
    digital =   models.BooleanField(default=False,null=True)
    #image
    def __str__(self):
        return self.name
class Order(models.Model):
    customer        =   models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_orderd     =   models.DateTimeField(auto_now_add=True)
    complete        =   models.BooleanField(default=False)
    transaction_Id  =   models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.id)
class OrderItem(models.Model):
    product     =   models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order       =   models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity    =   models.IntegerField(default=0,null=True,blank=True)
    date_added  =   models.DateTimeField(auto_now_add=True)

