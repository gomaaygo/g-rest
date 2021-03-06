# Generated by Django 3.2.6 on 2021-10-25 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_itemsale_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda')),
                ('status', models.CharField(choices=[('closed', 'Fechada'), ('open', 'Aberto')], max_length=50, verbose_name='Status')),
                ('type_of_payment', models.CharField(choices=[('money', 'Dinheiro'), ('card', 'Cartão'), ('pix', 'Pix')], max_length=50, verbose_name='Tipo de Pagamento')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=14, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Total')),
                ('items', models.ManyToManyField(to='sale.ItemSale', verbose_name='Itens da Venda')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
