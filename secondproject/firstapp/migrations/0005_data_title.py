# Generated by Django 5.1 on 2024-09-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_data_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]
