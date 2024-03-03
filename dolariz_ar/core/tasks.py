import logging

from core.connectors import get_connector
from core.models import DollarType
from dolariz_ar.celery import app

logger = logging.getLogger(__name__)


@app.task(name="obtain_prices_by_type_of_quote")
def obtain_prices_by_type_of_quote(type_of_quote: int) -> str:
    """
    Saves in cache and db the buying and selling prices for a type of dollar.

    Arguments:
    - type_of_quote (int): type of dollar quote.
    """

    connector = get_connector(type_of_quote)()
    connector.save()
    logger.info("obtain_prices_by_type_of_quote task executed")
    return f"The {type_of_quote} dollar was obtained successfully."


@app.task(name="obtain_prices")
def obtain_prices() -> str:
    """
    Saves in cache and db the buying and selling prices for any type of dollar.
    """

    keys = DollarType.__labels__.keys()
    for key in keys:
        obtain_prices_by_type_of_quote.delay(key)
    logger.info("obtain_prices task executed")
    return "Obtain prices tasks was queued."
