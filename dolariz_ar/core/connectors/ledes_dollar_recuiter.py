import logging

from core.models import DollarType
from core.connectors.dollar_recuiter_byma import DollarRecuiterByma
from constants import LEDES_DOLLAR_URL

logger = logging.getLogger(__name__)


class LEDESDollarRecruiter(DollarRecuiterByma):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the MEP dollar from the web COnvert this request into a method
        """

        self.url = LEDES_DOLLAR_URL
        self.get_type_of_quote = DollarType.LEDES
        self.bond_value = "X20Y4"
        self.bondD_value = "XY4D"
        self.data = {
            "excludeZeroPxAndQty": True,
            "T2": True,
            "T1": False,
            "T0": False,
            "Content-Type": "application/json",
        }

        super().__init__()

    def get_prices_from_response(self) -> tuple[float]:
        """
        Get the buying and selling prices from the response of the web.

        Returns
        -------
        tuple[float]
            The buying and selling prices.
        """

        bond_buying_price = self.bond[0].get("vwap", None)
        bondD_selling_price = self.bondD[0].get("vwap", None)

        return bond_buying_price, bondD_selling_price
