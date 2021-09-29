# Imports
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField("Nome", max_length=200, null=False, blank=False)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Categoria"), 
                    null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=200, null=False, blank=False)
    description = models.TextField("Descrição", null=True, blank=True)
    value = models.DecimalField("Valor", decimal_places=2, max_digits=14,
                        validators=[MinValueValidator(0.00)], null=False)
    type_of_measure = models.CharField("Unidade de Medida", max_length=2, 
                        null=True, blank=True)
    unit_size = models.FloatField("Tamanho da Unidade", null=True, 
                        blank=True, validators=[MinValueValidator(0)])


    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Produto"), 
                        null=False, blank=False, 
                        on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantidade em Estoque", 
                        null=False, blank=False, default=0,
                        validators=[MinValueValidator(0)])
    quantity_min = models.PositiveIntegerField(verbose_name="Quantidade Mínima", 
                        null=False, blank=False, default=0, 
                        validators=[MinValueValidator(0)])


    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"

    def __str__(self):
        return self.product.name


class InputOfProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Produto"), 
                    null=False, blank=False, 
                    on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantidade", 
                        null=False, blank=False, default=0,
                        validators=[MinValueValidator(0)])
    entry_date = models.DateTimeField(verbose_name="Data de entrada",
                                      auto_now_add=True)
    expiration_date = models.DateField("Data de validade", null=True, blank=True)


    class Meta:
        verbose_name = "Entrada de Produto"
        verbose_name_plural = "Entrada de Produtos"

    def __str__(self):
        return str(self.product.name)

    def save(self, *args, **kwargs):
        stock = Stock.objects.get(product=self.product)
        stock.quantity += self.quantity
        stock.save()
        super(InputOfProduct, self).save()


class OutputOfProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Produto"), 
                    null=False, blank=False, 
                    on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantidade", 
                        null=False, blank=False, default=0,
                        validators=[MinValueValidator(0)])
    departure_date = models.DateTimeField(verbose_name="Data de saída",
                                      auto_now_add=True)


    class Meta:
        verbose_name = "Saída de Produto"
        verbose_name_plural = "Saída de Produtos"

    def __str__(self):
        return str(self.product.name)

    def save(self, *args, **kwargs):
        stock = Stock.objects.get(product=self.product)
        if self.quantity <= stock.quantity:
            stock.quantity -= self.quantity
            stock.save()
        else:
            raise ValidationError("Não possui quantidade suficiente desse produto!")
        super(OutputOfProduct, self).save()