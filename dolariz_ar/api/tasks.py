import logging

from bs4 import BeautifulSoup
from celery import Celery
from requests import get

logger = logging.getLogger(__name__)

celery_app = Celery("celery_app", broker="amqp://user:password@localhost:15672/")


@celery_app.task
def get_blue() -> str:
    """
    Get the buy and sell values of the free dollar from dolarhoy.com
    """
    logger.warning("\nFREE DOLLAR CHECK EXECUTED")
    URL = "https://www.dolarhoy.com/cotizaciondolarblue"
    response = get(URL)
    soup = BeautifulSoup(response.content, "lxml")
    buy, sell = (float(tag.string.removeprefix("$")) for tag in soup.select(".value"))
    logger.warning(f"Buy: {buy} | Sell: {sell}\n")
    return buy, sell
