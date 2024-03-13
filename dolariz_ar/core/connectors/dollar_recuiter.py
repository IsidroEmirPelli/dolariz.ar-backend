import logging

from bs4 import BeautifulSoup
from django.core.cache import cache
from requests import get

from constants import DEFAULT_PRICE_VALUE
from core.models import Dollar
from core.services import calc_variation

logger = logging.getLogger(__name__)


class DollarRecruiter:
    def __init__(self) -> None:
        logger.info(f"{self.__class__.__name__} instantiated.")

    def save(self):
        """
        Saves the dollar in the database.
        """

        type_of_quote = self.get_type_of_quote()
        try:
            old_prices = cache.get(str(type_of_quote))
        except Exception:
            old_prices = None

        variation_buying_price = DEFAULT_PRICE_VALUE
        variation_selling_price = DEFAULT_PRICE_VALUE

        if old_prices:
            variation_buying_price = calc_variation(
                float(old_prices["buying_price"]),
                self.get_buying_price()
            )
            variation_selling_price = calc_variation(
                float(old_prices["selling_price"]),
                self.get_selling_price()
            )

        value = {
            "buying_price": self.get_buying_price(),
            "selling_price": self.get_selling_price(),
            "variation_buying_price": variation_buying_price,
            "variation_selling_price": variation_selling_price,
        }

        cache.set(str(type_of_quote), value)
        logger.info(f"{type_of_quote} dollar has setted in the cache.")

        Dollar.objects.create(
            price_buy=self.get_buying_price(),
            price_sell=self.get_selling_price(),
            type_of_quote=type_of_quote,
        )

    def get_buying_price(self) -> float:
        """
        Returns the buying price of the dollar.
        """

        logger.info(
            f"{self.__class__.__name__} get_buying_price -> {self.buying_price}."
        )
        return self.buying_price

    def get_selling_price(self) -> float:
        """
        Returns the selling price of the dollar.
        """

        logger.info(
            f"{self.__class__.__name__} get_selling_price -> {self.selling_price}."
        )
        return self.selling_price

    def get_type_of_quote(self) -> int:
        """
        Returns the type of quote.
        """

        logger.info(
            f"{self.__class__.__name__} get_type_of_quote -> {self.type_of_quote}."
        )
        return self.type_of_quote
