# Generated by Django 4.0.6 on 2024-03-01 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDefCategory',
            new_name='Category',
        ),
    ]
