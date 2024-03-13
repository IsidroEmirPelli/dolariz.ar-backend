import logging

from django.core.cache import cache
from constants import DEFAULT_PRICE_VALUE

from .models import Dollar, DollarType

logger = logging.getLogger(__name__)


def calc_variation(old_price: float, new_price: float) -> float:
    """
    Calculate the variation between the old and new price.
    """

    return ((new_price / old_price) - 1) * 100


def save_dollar_prices_in_cache(
    buying_price: float,
    selling_price: float,
    type_of_quote: int
) -> None:
        try:
            old_prices = cache.get(str(type_of_quote))
        except Exception:
            old_prices = None
        if old_prices:
            variation_buying_price = calc_variation(
                float(old_prices["buying_price"]),
                buying_price
            )
            variation_selling_price = calc_variation(
                float(old_prices["selling_price"]),
                selling_price
            )
        else:
            variation_buying_price = DEFAULT_PRICE_VALUE
            variation_selling_price = DEFAULT_PRICE_VALUE
        value = {
            "buying_price": buying_price,
            "selling_price": selling_price,
            "variation_buying_price": variation_buying_price,
            "variation_selling_price": variation_selling_price,
        }
        cache.set(str(type_of_quote), value)
        logger.info(f"{type_of_quote} dollar has setted in the cache.")


def save_dollar_prices_in_db(
    buying_price: float,
    selling_price: float,
    type_of_quote: int
) -> None:
    Dollar.objects.create(
        price_buy=buying_price,
        price_sell=selling_price,
        type_of_quote=type_of_quote,
    )
    logger.info(f"{type_of_quote} dollar added to the database.")


def get_dollar_prices_from_db_service(
    type_of_quote: DollarType,
) -> tuple[float, float]:
    """
    Get the buying and selling prices for the dollar from the database.
    """

    dollar = Dollar.objects.get(type_of_quote=type_of_quote)
    logger.info(f"Got the {type_of_quote} dollar prices from the database.")
    return dollar.price_buy, dollar.price_sell


def get_dollar_prices_and_variations_from_cache_service(
    type_of_quote: DollarType,
) -> tuple[float, float, float, float]:
    """
    Get the buying and selling prices for the dollar from the cache.
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
