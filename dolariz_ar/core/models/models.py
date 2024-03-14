from django.db.models import CharField, DateTimeField, DecimalField, JSONField, Model
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django_enumfield import enum

from .enums import DollarType


def generate_dollar_uuid():
    """
    Generate a random UUID for the uuid field of the dollar model.
    """

    return "dollar_" + get_random_string(length=9)


class Dollar(Model):
    """
    Dollar model to store the buying and selling dollar prices of any type of dollar in Argentina.

    Attributes:
    - uuid (CharField): Unique UUID for the dollar.
    - price_buy (DecimalField): Price to buy the dollar.
    - price_sell (DecimalField): Price to sell the dollar.
    - date (DateTimeField): Date and time of the prices of the dollar.
    - type_of_quote (EnumField): Type of dollar quote.
    - extra_data (JSONField): Extra data for the dollar.
    """

    uuid = CharField(
        max_length=16,
        default=generate_dollar_uuid,
        primary_key=True,
        help_text=_("Unique UUID for the dollar"),
    )
    price_buy = DecimalField(
        max_digits=10, decimal_places=2, help_text=_("Price to buy the dollar")
    )
    price_sell = DecimalField(
        max_digits=10, decimal_places=2, help_text=_("Price to sell the dollar")
    )
    date = DateTimeField(auto_now_add=True, help_text=_("Date and time of the dollar"))
    type_of_quote = enum.EnumField(DollarType, help_text=_("Type of quote"))
    extra_data = JSONField(
        help_text=_("Extra data for the dollar"),
        default=dict,
    )

    def __str__(self):
        return f"{self.type_of_quote} - {self.price_buy} - {self.price_sell}"
