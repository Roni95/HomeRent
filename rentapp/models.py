
from datetime import datetime
from email.headerregistry import Address
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from httpx import request

User = get_user_model()

class RentPost(models.Model):
    date = models.DateField(auto_now=True)
    rent_ammount = models.IntegerField(verbose_name="Cost")
    room = models.IntegerField(verbose_name="Total Room")
    address = models.TextField(verbose_name="Address", default='')
    post = models.TextField(
        verbose_name="Extra Informaion(Bed Room, Kitchen, Bathroom etc)", default='')
    mobile = models.CharField(
        max_length=11, verbose_name="contact info", default='')
    postby = User

    def __str__(self):
        return self.post
