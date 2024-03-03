from rest_framework.serializers import ModelSerializer

from .models import Dollar


class DollarSerializer(ModelSerializer):
    class Meta:
        model = Dollar
        fields = [
            "price_buy",
            "price_sell",
            "date",
            "type_of_quote",
            "extra_data",
        ]
