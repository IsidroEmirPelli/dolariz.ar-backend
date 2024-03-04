from rest_framework.serializers import ModelSerializer, Serializer
from django.db.models import DecimalField

from .models import Dollar


class DollarSerializer(ModelSerializer):
    """
    Serializer for the Dollar model.
    
    Attributes:
    - price_buy (FloatField): Price to buy the dollar.
    - price_sell (FloatField): Price to sell the dollar.
    - date (DateTimeField): Date and time of the prices of the dollar.
    - type_of_quote (EnumField): Type of dollar quote.
    - extra_data (JSONField): Extra data for the dollar.
    """

    class Meta:
        model = Dollar
        fields = [
            "price_buy",
            "price_sell",
            "date",
            "type_of_quote",
            "extra_data",
        ]


class CacheDollarSerializer(Serializer):
    """
    Serializer for the Dollar model to be used in the cache.
    
    Attributes:
    - buying_price (DecimalField): Price to buy the dollar.
    - selling_price (DecimalField): Price to sell the dollar.
    - variation_buying_price (DecimalField): Variation of the buying price.
    - variation_selling_price (DecimalField): Variation of the selling price.
    """

    buying_price = DecimalField()
    selling_price = DecimalField()
    variation_buying_price = DecimalField()
    variation_selling_price = DecimalField()
