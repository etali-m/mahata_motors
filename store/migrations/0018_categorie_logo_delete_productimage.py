# Generated by Django 4.1.7 on 2023-09-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_images_delete_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ), 
    ]
