

# Create your models here.
from django.db import models


class Test(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
