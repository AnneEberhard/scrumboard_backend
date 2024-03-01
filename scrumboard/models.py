from datetime import date
from django import apps
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

from contacts.models import Contact



"""
This models defines the tasks
"""
class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=15, default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=30, default='')
    assignedContacts = models.ManyToManyField(Contact)
    dueDate = models.DateField(default=date.today)
    prio = models.CharField(max_length=15, default='')
    column = models.CharField(max_length=50, default='')
    
"""
This models defines the subtasks
"""
class Subtask(models.Model):
    subTaskName = models.TextField(default='')
    subTaskDone = models.BooleanField(default=False)
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)

"""
This models defines the user defined categories
"""
class UserDefCategory(models.Model):
    name = models.CharField(max_length=15)
    colorCode = models.CharField(max_length=15)

"""
This models extends the baseUserManager model and is needed for a correct password creation
"""
class UserManager(BaseUserManager):
    use_in_migration = True
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)