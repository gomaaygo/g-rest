# Generated by Django 3.2.6 on 2021-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0012_itemsale_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsale',
            name='status',
            field=models.CharField(blank=True, choices=[('canceled', 'Cancelado')], max_length=50, null=True, verbose_name='Status'),
        ),
    ]
