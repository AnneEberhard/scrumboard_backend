from django.db import models
from datetime import date
from django.conf import settings#

from contacts.models import Contact

"""
This models defines the tasks
"""
class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=30, default='')
    assignedContacts = models.ManyToManyField(Contact)
    dueDate = models.DateField(default=date.today)
    prio = models.CharField(max_length=15, default='')
    column = models.CharField(max_length=50, default='')
    
