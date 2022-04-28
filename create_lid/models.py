from django.db import models


# Create your models here.
class LidModels(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
