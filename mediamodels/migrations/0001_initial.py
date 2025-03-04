# Generated by Django 5.1.5 on 2025-03-01 18:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organiqueFood', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desctptions', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='Items')),
                ('price', models.DecimalField(decimal_places=2, max_digits=2000)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stars', models.PositiveIntegerField(null=True)),
                ('still_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='mediamodels.category')),
                ('filters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filter', to='organiqueFood.productsfilter')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
