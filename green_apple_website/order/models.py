from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, default='customer name')
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    total_items = models.IntegerField()
    message = models.CharField(max_length=500)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    selected_item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
