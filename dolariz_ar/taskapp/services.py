from core.connectors import (
    OfficialDollarRecruiter,
    BlueDollarRecruiter,
    MEPDollarRecruiter,
    CCLDollarRecruiter,
    LEDESDollarRecruiter,
)
from core.models import DollarType


def get_connector(type_of_quote: int):
    return {
        DollarType.OFFICIAL: OfficialDollarRecruiter,
        DollarType.BLUE: BlueDollarRecruiter,
        DollarType.MEP: MEPDollarRecruiter,
        DollarType.CCL: CCLDollarRecruiter,
        DollarType.LEDES: LEDESDollarRecruiter,
    }[type_of_quote]
