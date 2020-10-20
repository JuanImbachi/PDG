# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DengueCase(models.Model):
    city = models.CharField(max_length=50)
    notification_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=50)