# Generated by Django 4.0.6 on 2024-02-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0010_remove_task_assignedcontacts_task_assignedcontacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(blank=True, to='scrumboard.subtask'),
        ),
    ]