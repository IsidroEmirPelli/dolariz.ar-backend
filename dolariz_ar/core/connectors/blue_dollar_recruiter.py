import logging

from bs4 import BeautifulSoup
from requests import get

from constants import BLUE_DOLLAR_URL

from core.models import DollarType

from core.connectors.dollar_recruiter import DollarRecruiter

logger = logging.getLogger(__name__)


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
