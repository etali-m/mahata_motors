# Generated by Django 4.1.7 on 2023-04-24 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_categorie_parent_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sous_categories', to='store.categorie'),
        ),
    ]
