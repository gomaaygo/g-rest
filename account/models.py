from django.db import models
from django.contrib.auth.models import User


class Account(User):
    TYPE_USER_CHOICES = (
        ("cashier", "Caixa"),
        ("waiter", "Garçom"),
        ("manager", "Gestor"),
    )
    type_user = models.CharField(
        "Tipo de Usuário", max_length=50, null=False, blank=False,
         choices=TYPE_USER_CHOICES
    )
    changed_pass = models.BooleanField("Trocou senha?", default=False)

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return self.username
