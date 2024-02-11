from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    acronym = models.CharField(max_length=3)
    color = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class UserDefCategory(models.Model):
    title = models.CharField(max_length=15)
    color = models.CharField(max_length=15)


class Task(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=15)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=15)
    column_category = models.CharField(max_length=15)
    subtasks = models.TextField(blank=True, default='[]')
