# Generated by Django 4.0.6 on 2024-02-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_contact_alter_task_author_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freeColorCode', models.CharField(max_length=15)),
            ],
        ),
    ]