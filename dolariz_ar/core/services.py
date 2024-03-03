from .models import Dollar, DollarType


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


def get_official_dollar_prices_from_cache_service(
    type_of_quote: DollarType,
) -> tuple[float, float]:
    """
    Get the buying and selling prices for the blue dollar from the cache.
    """

    dollar = Dollar.objects.get(type_of_quote=type_of_quote)
    return dollar.price_buy, dollar.price_sell
