# Generated by Django 4.0.6 on 2024-02-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0011_alter_task_subtasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='description',
            new_name='subTaskName',
        ),
        migrations.AddField(
            model_name='subtask',
            name='subTaskDone',
            field=models.BooleanField(default=False),
        ),
    ]
