# Generated by Django 4.0.6 on 2024-03-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0020_delete_contact_alter_task_assignedcontacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDefCategory',
        ),
    ]
