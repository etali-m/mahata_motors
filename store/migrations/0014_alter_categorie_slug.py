# Generated by Django 4.1.7 on 2023-06-19 07:20

import autoslug.fields
from django.db import migrations
import django.utils.text


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_categorie_parent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=django.utils.text.slugify, unique=True),
        ),
    ]
