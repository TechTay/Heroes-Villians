from django.db import models
from super_types.models import SuperType
# Create your models here.

class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    supers = models.ForeignKey(SuperType, on_delete=models.CASCADE)