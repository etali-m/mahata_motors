# Generated by Django 4.1.7 on 2023-10-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_brand_origine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipement',
            old_name='brand',
            new_name='fabirquant',
        ),
    ]