# Generated by Django 5.1 on 2024-09-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_data_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='slug',
            field=models.CharField(default='title', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(default='a title', max_length=100),
        ),
    ]
