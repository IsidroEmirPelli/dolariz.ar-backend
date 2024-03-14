import logging
from constants import MEP_DOLLAR_URL

from core.models import DollarType

from core.connectors.dollar_recuiter_byma import DollarRecruiterByma

logger = logging.getLogger(__name__)


class MEPDollarRecruiter(DollarRecruiterByma):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the MEP dollar from the web
        """

        self.url = MEP_DOLLAR_URL
        self.type_of_quote = DollarType.MEP
        self.bond_value = "AL30"
        self.bondD_value = "AL30D"
        self.data = {"page_number": 1}

        super().__init__()
