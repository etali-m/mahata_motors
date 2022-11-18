# Generated by Django 4.1.3 on 2022-11-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'administrator'), ('SELLER', 'seller'), ('CUSTOMER', 'customer')], default='CUSTOMER', max_length=30),
        ),
    ]