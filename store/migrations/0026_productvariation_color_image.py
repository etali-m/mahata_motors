# Generated by Django 4.1.7 on 2023-11-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_images_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='color_image',
            field=models.ImageField(blank=True, null=True, upload_to='color_variations/'),
        ),
    ]
