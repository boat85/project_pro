from unicodedata import name
from django.db import models

# Create your models here.

class friends(models.Model):
  name = models.CharField(max_length=50)
  sex = models.IntegerField(max_length=1)
  detail = models.TextField()