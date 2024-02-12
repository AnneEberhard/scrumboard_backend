from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Contact(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    acronym = models.CharField(max_length=3)
    color = models.CharField(max_length=15)
    


class UserDefCategory(models.Model):
    title = models.CharField(max_length=15)
    color = models.CharField(max_length=15)


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=15)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=15)
    column_category = models.CharField(max_length=15)
    subtasks = models.TextField(blank=True, default='[]')
