# Generated by Django 3.2.6 on 2021-11-25 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0010_alter_sale_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsale',
            name='quantity_snack',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Quantidade (Kg/g)'),
        ),
        migrations.AlterField(
            model_name='itemsale',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade'),
        ),
    ]