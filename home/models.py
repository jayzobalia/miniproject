from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)