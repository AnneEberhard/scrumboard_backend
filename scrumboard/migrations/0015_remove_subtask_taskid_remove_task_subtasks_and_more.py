# Generated by Django 4.0.6 on 2024-02-17 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0014_alter_task_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='taskId',
        ),
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scrumboard.task'),
            preserve_default=False,
        ),
    ]
