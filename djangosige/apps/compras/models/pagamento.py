# -*- coding: utf-8 -*-

from django.utils.formats import localize
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Tabela diferente das vendas.
class Pagamento(models.Model):
    compra_id = models.ForeignKey(
        'compras.Compra', related_name="parcela_pagamento", on_delete=models.CASCADE)
    indice_parcela = models.IntegerField()
    vencimento = models.DateField()
    valor_parcela = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))])

    @property
    def format_valor_parcela(self):
        return localize(self.valor_parcela)

    @property
    def format_vencimento(self):
        return self.vencimento.strftime('%d/%m/%Y')
