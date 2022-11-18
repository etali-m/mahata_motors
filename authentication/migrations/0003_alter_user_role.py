# Generated by Django 4.1.3 on 2022-11-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CUSTOMER', 'customer'), ('SELLER', 'seller'), ('ADMIN', 'administrator')], default='CUSTOMER', max_length=30),
        ),
    ]