from django.db import models
from tasks.models import Task


"""
This models defines the subtasks
"""
class Subtask(models.Model):
    subTaskName = models.TextField(default='')
    subTaskDone = models.BooleanField(default=False)
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)

