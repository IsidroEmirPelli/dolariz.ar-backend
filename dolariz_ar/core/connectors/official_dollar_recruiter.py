import logging

from bs4 import BeautifulSoup
from requests import get

from constants import OFFICIAL_DOLLAR_URL

from core.models import DollarType

from core.connectors.dollar_recruiter import DollarRecruiter

logger = logging.getLogger(__name__)


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
