from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    meter_number = models.CharField(max_length=100, default='0000')

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.user.username

class Due(models.Model):
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.user.username