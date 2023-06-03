from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    meter_number = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    units = models.FloatField(default=0.0)
    status = models.BooleanField(
        choices=[
            (True, 'Active'),
            (False, 'Blocked')
        ]
    )

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.customer.user.username} => {self.amount}'