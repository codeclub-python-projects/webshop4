from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0.0)
    photo = models.FileField(null=False, upload_to='upload/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    address = models.CharField(max_length=500, null=False)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    open_date = models.DateTimeField(null=False, auto_now=True)
    close_date = models.DateTimeField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=False, default=1)
    delivery = models.ForeignKey(Delivery, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} / {self.user}'


class Comment(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(null=False, auto_now=True)
    comment_text = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f'{self.delivery} / {self.manager}'
