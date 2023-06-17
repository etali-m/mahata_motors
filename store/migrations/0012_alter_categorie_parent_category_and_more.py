# Generated by Django 4.1.7 on 2023-04-24 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_categorie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sous_categorie', to='store.categorie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='store.categorie'),
        ),
    ]
