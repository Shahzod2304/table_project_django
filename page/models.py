from django.db import models

# Create your models here.
class Employee(models.Model):
    Id = models.CharField(max_length=10)
    FIO = models.CharField(max_length=100)
    kun1 = models.CharField(max_length=100)
    kun2 = models.CharField(max_length=100)
    kun3 = models.CharField(max_length=100)
    kun4 = models.CharField(max_length=100)
    kun5 = models.CharField(max_length=100)
    jami = models.CharField(max_length=100)
    
