import logging

from core.models import DollarType

from core.connectors.dollar_recruiter import DollarRecruiter

logger = logging.getLogger(__name__)


class CCLDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the CCL dollar from the web.
        """

        super().__init__()
        self.type_of_quote = DollarType.CCL.value
