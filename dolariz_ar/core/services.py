import logging

from django.core.cache import cache

from .models import Dollar, DollarType

logger = logging.getLogger(__name__)


def calc_variation(old_price: float, new_price: float) -> float:
    """
    Calculate the variation between the old and new price.
    """

    return ((new_price / old_price) - 1) * 100


def save_dollar_prices_in_db(
    get_buying_price: float,
    get_selling_price: float,
    type_of_quote: int
) -> None:
    Dollar.objects.create(
        price_buy=get_buying_price(),
        price_sell=get_selling_price(),
        type_of_quote=type_of_quote,
    )
    logger.info(f"{type_of_quote} dollar added to the database.")


def get_official_dollar_prices_from_db_service(
    type_of_quote: DollarType,
) -> tuple[float, float]:
    """
    Get the buying and selling prices for the blue dollar from the database.
    """

    dollar = Dollar.objects.get(type_of_quote=type_of_quote)
    logger.info(f"Got the {type_of_quote} dollar prices from the database.")
    return dollar.price_buy, dollar.price_sell


def get_official_dollar_prices_and_variations_from_cache_service(
    type_of_quote: DollarType,
) -> tuple[float, float, float, float]:
    """
    Get the buying and selling prices for the blue dollar from the cache.
    """

    cached = cache.get(str(type_of_quote))
    prices = {
        "buying_price": cached["buying_price"],
        "selling_price": cached["selling_price"],
        "variation_buying_price": cached["variation_buying_price"],
        "variation_selling_price": cached["variation_selling_price"],
    }
    logger.info(
        f"Got the {type_of_quote} dollar prices and variations from the cache.")
    return prices
