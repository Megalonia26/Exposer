# Generated by Django 5.1.5 on 2025-03-02 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediamodels', '0007_remove_product_slug'),
        ('organiqueFood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filter', to='organiqueFood.productsfilter'),
        ),
    ]
