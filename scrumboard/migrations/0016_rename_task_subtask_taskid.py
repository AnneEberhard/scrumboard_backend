# Generated by Django 4.0.6 on 2024-02-17 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0015_remove_subtask_taskid_remove_task_subtasks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='task',
            new_name='taskId',
        ),
    ]
