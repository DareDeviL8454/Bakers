from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # phone = models.CharField(max_length=10)
    desc = models.TextField()


class Checkout1(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    quantity = models.CharField(max_length=20)
    # phone = models.CharField(max_length=10)


class Index(models.Model):
    shop_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images")
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)  # available / not
    time = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)


class Menu(models.Model):
    shop_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images")
    des = models.CharField(max_length=200)
    price = models.IntegerField()


class Payement(models.Model):
    qr = models.ImageField(upload_to="Images")