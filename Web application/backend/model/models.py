# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DengueCase(models.Model):
    City = models.CharField(max_length=50)
    NotificationDate = models.DateField()
    Age = models.DecimalField(max_digits=4, decimal_places=2)
    Gender = models.CharField(max_length=10)
    Neighborhood = models.CharField(max_length=50)
    Commune = models.CharField(max_length=10)
