from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    valuation=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


