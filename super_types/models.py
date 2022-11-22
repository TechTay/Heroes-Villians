from django.db import models
from supers.models import Supers
# Create your models here.

class SuperType(models.Model):
    type = models.CharField(max_length=255)
    supers = models.ForeignKey(Supers, on_delete=models.CASCADE)