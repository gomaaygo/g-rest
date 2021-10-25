# Imports
from django.db import models
from product.models import Product
from django.core.validators import MinValueValidator


class Card(models.Model):
    STATUS_CARD = (
        ("available", "Disponível"),
        ("not_available", "Não Disponível"),
    )
    status = models.CharField(
        "Status", max_length=50, null=False, blank=False,
         choices=STATUS_CARD)

    class Meta:
        verbose_name="Ficha"
        verbose_name_plural="Fichas"

    def __str__(self):
        return self.status


class ItemSale(models.Model):
    product = models.ForeignKey(Product, verbose_name="Produto", 
                null=False, blank=False, 
                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantidade", 
                        null=False, blank=False, default=0,
                        validators=[MinValueValidator(0)])
    unitary_value = models.DecimalField("Valor Unitário", decimal_places=2, max_digits=14,
                        validators=[MinValueValidator(0.00)], null=False)
    total = models.DecimalField("Total", decimal_places=2, max_digits=14,
                        validators=[MinValueValidator(0.00)], null=False, default=0)

    class Meta:
        verbose_name="Item de Venda"
        verbose_name_plural="Itens de Venda"

    def __str__(self):
        return str(self.product)


class Sale(models.Model):
    STATUS_SALE = (
        ("closed", "Fechada"),
        ("open", "Aberto"),
    )
    TYPE_OF_PAYMENT = (
        ("money", "Dinheiro"),
        ("card", "Cartão"),
        ("pix", "Pix"),
    )
    sale_date = models.DateTimeField(verbose_name="Data da Venda",
                                      auto_now_add=True)
    items = models.ManyToManyField(ItemSale, verbose_name="Itens da Venda")
    status = models.CharField(
        "Status", max_length=50, null=False, blank=False,
         choices=STATUS_SALE)
    type_of_payment = models.CharField(
        "Tipo de Pagamento", max_length=50, null=False, blank=False,
         choices=TYPE_OF_PAYMENT)
    total = models.DecimalField("Total", decimal_places=2, max_digits=14,
                    validators=[MinValueValidator(0.00)], null=False, default=0)

    class Meta:
        verbose_name="Venda"
        verbose_name_plural="Vendas"

    def __str__(self):
        return self.status