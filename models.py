# from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#
class Products(models.Model):
    prd_name=models.CharField(max_length=100)
    prd_price=models.FloatField()
    stock = models.IntegerField(default=1)
    prd_img=models.ImageField(upload_to='Products')
    prd_description = models.TextField()
    def __str__(self):
        return self.prd_name

class categories(models.Model):
    title = models.CharField(max_length=200, unique=True)
        # descripsion = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='cat-photo')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def get_product_price(self):
        price = [self.product.price]
        return sum(price)

class Services(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='Products')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name







#
#
#     class Meta:
#         db_table="registration"
# #
# # class login_details(models.Model):
# #     email = models.CharField(max_length=20)
# #     password = models.CharField(max_length=30)
# # class login_details(models.Model):
# #     email = models.CharField(max_length=200)
# #     password = models.CharField(max_length=200)
#
# class login(models.Model):
#     email=models.CharField(max_length=200)
#     pwd1=models.CharField(max_length=200)
#     class Meta:
#         db_table="login"
