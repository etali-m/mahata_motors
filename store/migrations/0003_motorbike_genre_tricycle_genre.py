# Generated by Django 4.1.7 on 2023-02-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_brand_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorbike',
            name='genre',
            field=models.CharField(default='Moto', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='tricycle',
            name='genre',
            field=models.CharField(default='Tricycle', editable=False, max_length=50),
        ),
    ]
