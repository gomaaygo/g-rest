# Generated by Django 3.2.6 on 2022-04-05 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0014_alter_sale_type_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsale',
            name='quantity_snack',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=14, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Quantidade (Kg/g)'),
        ),
    ]