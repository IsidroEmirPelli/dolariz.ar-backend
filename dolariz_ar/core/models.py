from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django_enumfield import enum

from .enums import DolarType


def generate_dolar_uuid():
    return "dolar_" + get_random_string(length=10)


class Dolar(models.Model):
    uuid = models.CharField(
        max_length=16,
        default=generate_dolar_uuid,
        primary_key=True,
        help_text=_("Unique UUID for the dolar")
    )
    price_buy = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_("Price to buy the dolar")
    )
    price_sell = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_("Price to sell the dolar")
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date and time of the dolar")
    )
    type_of_quote = enum.EnumField(
        DolarType,
        max_length=10,
        help_text=_("Type of quote")
    )
