# Generated by Django 4.1.7 on 2023-10-28 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_moto_annee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_type', models.CharField(choices=[('color', 'Color'), ('size', 'Size')], max_length=10)),
                ('value', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
