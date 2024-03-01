
from django.db import models

"""
This models defines the contacts
"""
class Contact(models.Model):
    user_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    acronym = models.CharField(max_length=3)
    color = models.CharField(max_length=15)
