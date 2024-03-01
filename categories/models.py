from django.db import models

"""
This models defines the user defined categories
"""
class Category(models.Model):
    name = models.CharField(max_length=15)
    colorCode = models.CharField(max_length=15)
