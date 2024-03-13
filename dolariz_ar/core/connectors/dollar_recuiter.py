import logging

from core.services import (
    save_dollar_prices_in_db,
    save_dollar_prices_in_cache
)

logger = logging.getLogger(__name__)


class DollarRecruiter:
    def __init__(self) -> None:
        logger.info(f"{self.__class__.__name__} instantiated.")

    def save(self):
        """
        Stores dollar prices in the cache and database.
        """

        type_of_quote = self.get_type_of_quote()
        buying_price = self.get_buying_price()
        selling_price = self.get_selling_price()
        save_dollar_prices_in_cache(
            buying_price,
            selling_price,
            type_of_quote
        )
        save_dollar_prices_in_db(
            buying_price,
            selling_price,
            type_of_quote
        )
        logger.info(
            f"{self.__class__.__name__} save -> B{buying_price}-S{selling_price}-T{type_of_quote}."
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
