from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django_enumfield import enum

from .enums import DollarType


def generate_dollar_uuid():
    return "dollar_" + get_random_string(length=9)


class Dollar(models.Model):
    uuid = models.CharField(
        max_length=16,
        default=generate_dollar_uuid,
        primary_key=True,
        help_text=_("Unique UUID for the dollar")
    )
    price_buy = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_("Price to buy the dollar")
    )
    price_sell = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_("Price to sell the dollar")
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date and time of the dollar")
    )
    type_of_quote = enum.EnumField(
        DollarType,
        help_text=_("Type of quote")
    )
    extra_data = models.JSONField(
        help_text=_("Extra data for the dollar"),
        default=dict,
    )

    def __str__(self):
        return f"{self.type_of_quote} - {self.price_buy} - {self.price_sell}"