import logging

from core.models import DollarType

from core.connectors.dollar_recuiter import DollarRecruiter

logger = logging.getLogger(__name__)


class LEDESDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the LEDES dollar from the web.
        """

        super().__init__()
        self.type_of_quote = DollarType.LEDES.value
