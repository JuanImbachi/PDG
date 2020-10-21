# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DengueCase(models.Model):
    City = models.CharField(max_length=50)
    OccurrenceMonth = models.CharField(max_length=20)
    NotificationDate = models.DateField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Neighborhood = models.CharField(max_length=50)
    Commune = models.CharField(max_length=10)
