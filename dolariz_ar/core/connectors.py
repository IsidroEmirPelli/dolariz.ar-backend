import logging

from bs4 import BeautifulSoup
from requests import get

from constants import (
    BLUE_DOLLAR_URL,
    OFFICIAL_DOLLAR_URL
)

from .models import DollarType
from .services import (
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


class OfficialDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Get the buying and selling prices for the official dollar from the web.
        """

        super().__init__()
        soup = BeautifulSoup(get(OFFICIAL_DOLLAR_URL).content, "lxml")
        prices = (
            soup.find("div", id="divisas")
            .find(string="Dolar U.S.A")
            .parent.parent.find_all("td")[1:]
        )
        self.buying_price = float(prices[0].string)
        self.selling_price = float(prices[1].string)
        self.type_of_quote = DollarType.OFFICIAL.value


class BlueDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Get the buying and selling prices for the blue dollar from the web.
        """

        super().__init__()
        soup = BeautifulSoup(get(BLUE_DOLLAR_URL).content, "lxml")
        prices = (
            soup.find("section", class_="modulo__cotizaciones")
            .find("a", string="Dólar blue")
            .parent
        )
        self.buying_price = float(
            prices.find("div", class_="compra")
            .find("div", class_="val")
            .string.removeprefix("$")
        )
        self.selling_price = float(
            prices.find("div", class_="venta")
            .find("div", class_="val")
            .string.removeprefix("$")
        )
        self.type_of_quote = DollarType.BLUE.value


class MEPDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the MEP dollar from the web.
        """

        super().__init__()
        self.type_of_quote = DollarType.MEP.value


class CCLDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the CCL dollar from the web.
        """

        super().__init__()
        self.type_of_quote = DollarType.CCL.value


class LEDESDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the LEDES dollar from the web.
        """

        super().__init__()
        self.type_of_quote = DollarType.LEDES.value


def get_connector(type_of_quote: int):
    return {
        DollarType.OFFICIAL: OfficialDollarRecruiter,
        DollarType.BLUE: BlueDollarRecruiter,
        DollarType.MEP: MEPDollarRecruiter,
        DollarType.CCL: CCLDollarRecruiter,
        DollarType.LEDES: LEDESDollarRecruiter,
    }[type_of_quote]
