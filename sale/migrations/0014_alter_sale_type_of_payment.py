# Generated by Django 3.2.6 on 2022-01-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0013_alter_itemsale_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type_of_payment',
            field=models.CharField(blank=True, choices=[('money', 'Dinheiro'), ('pix', 'Pix'), ('credit', 'Crédito'), ('debit', 'Débito')], max_length=50, null=True, verbose_name='Tipo de Pagamento'),
        ),
    ]
