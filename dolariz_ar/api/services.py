import logging

from core.models import Dollar
from core.services import (
    get_official_dollar_prices_and_variations_from_cache_service,
    calc_variation,
)

logger = logging.getLogger(__name__)


def get_dollar_price_by_type_of_quote(type_of_quote: str) -> dict:
    data = None
    try:
        data = get_official_dollar_prices_and_variations_from_cache_service(
            type_of_quote
        )
        if not data:
            prices = (
                Dollar.objects
                .filter(type_of_quote=type_of_quote)
                .latest("date")[:2]
            )
            variation_buying_price = calc_variation(
                prices[1].price_buy,
                prices[0].price_buy
            ),
            variation_selling_price = calc_variation(
                prices[1].price_sell,
                prices[0].price_sell
            )
            data = {
                "buying_price": prices[0].price_buy,
                "selling_price": prices[0].price_sell,
                "variation_buying_price": variation_buying_price,
                "variation_selling_price": variation_selling_price,
            }
    except Exception as e:
        logger.error(
            f"get_dollar_price_by_type_of_quote obtain_price -> Error obtaining the dollar price: {e}"
        )
    return data
