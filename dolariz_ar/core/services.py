from .models import Dollar, DollarType
from django.core.cache import cache


def calc_variation(old_price: float, new_price: float) -> float:
    """
    Calculate the variation between the old and new price.
    """

    return ((new_price / old_price) - 1) * 100


def get_official_dollar_prices_from_db_service(
    type_of_quote: DollarType,
) -> tuple[float, float]:
    """
    Get the buying and selling prices for the blue dollar from the database.
    """

    dollar = Dollar.objects.get(type_of_quote=type_of_quote)
    return dollar.price_buy, dollar.price_sell


def get_official_dollar_prices_and_variations_from_cache_service(
    type_of_quote: DollarType,
) -> tuple[float, float, float, float]:
    """
    Get the buying and selling prices for the blue dollar from the cache.
    """

    cached = cache.get(type_of_quote)
    prices = {
        "buying_price": cached["buying_price"],
        "selling_price": cached["selling_price"],
        "variation_buying_price": cached["variation_buying_price"],
        "variation_selling_price": cached["variation_selling_price"],
    }
    return prices
