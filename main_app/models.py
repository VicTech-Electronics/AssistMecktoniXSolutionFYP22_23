from django.db import models

# Create your models here.
class Detail(models.Model):
    title = models.CharField(max_length=10)
    flowrate = models.FloatField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class State(models.Model):
    title = models.CharField(max_length=10)
    value = models.Choices