from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Daysmatter_calendar(models.Model):
    name=models.CharField(max_length=100)
    descriptions=models.TextField()
    date=models.DateTimeField()
    created=models.DateTimeField(auto_now_add=True)
