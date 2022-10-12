from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    phone = models.IntegerField(max_value=100)
    address_city = models.CharField(max_length=500)

