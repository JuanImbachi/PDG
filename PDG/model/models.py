from django.db import models
from django.contrib.auth.models import User

class DengueRegister(models.Model):
    title = models.TextField(max_length=300)
