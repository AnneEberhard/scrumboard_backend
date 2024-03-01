# Generated by Django 4.0.6 on 2024-03-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('scrumboard', '0019_alter_task_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='task',
            name='assignedContacts',
            field=models.ManyToManyField(to='contacts.contact'),
        ),
    ]
