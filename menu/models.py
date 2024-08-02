from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    nameOfUser=models.CharField(max_length=250)
    email_id=models.EmailField()
    subjectOfQuery=models.CharField(max_length=240)
    queryMessage=models.TextField()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    fullName = models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email_id=models.EmailField()
    ph_num = models.CharField(max_length=10)
    cart_items=models.JSONField()
    totalAmount=models.IntegerField(default=0)
    is_paid=models.BooleanField()
    payment_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    order_placed_time=models.DateTimeField(auto_now_add=True)
    order_complete_time=models.DateTimeField(null=True,blank=True)
    order_status=models.CharField(max_length=255,default='Received')


class OrderStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id=models.CharField(max_length=255)
    order_status = models.CharField(max_length=255, default='Received')
    time_status=models.DateTimeField(auto_now_add=True)
