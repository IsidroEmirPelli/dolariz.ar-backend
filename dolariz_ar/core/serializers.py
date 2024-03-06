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
