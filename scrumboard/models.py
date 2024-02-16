from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Contact(models.Model):
    user_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    acronym = models.CharField(max_length=3)
    color = models.CharField(max_length=15)


class Subtask(models.Model):
    subTaskName = models.TextField(default='')
    subTaskDone = models.BooleanField(default=False)
    taskId = models.IntegerField(default=0)


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=15, default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=30, default='')
    assignedContacts = models.ManyToManyField(Contact)
    dueDate = models.DateField(default=date.today)
    prio = models.CharField(max_length=15, default='')
    subtasks = models.ManyToManyField(Subtask, blank=True)
    column = models.CharField(max_length=50, default='')
    

class UserDefCategory(models.Model):
    name = models.CharField(max_length=15)
    colorCode = models.CharField(max_length=15)


class FreeColor(models.Model):
    freeColorCode = models.CharField(max_length=15)
