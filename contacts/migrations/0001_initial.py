# Generated by Django 4.0.6 on 2024-03-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('acronym', models.CharField(max_length=3)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]
