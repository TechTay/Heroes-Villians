from django.db import models

# Create your models here.

class SuperType(models.Model):
    model = models.CharField(max_length=255)    