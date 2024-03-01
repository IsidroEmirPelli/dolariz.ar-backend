import logging

from bs4 import BeautifulSoup
from constants import DOLLAR_SCRAPPER_URL as url
from requests import get

from .celery import app

logger = logging.getLogger(__name__)

@app.task
def get_free() -> str:
    """
    Get the buy and sell values of the free dollar from dolarhoy.com
    """
    logger.warning("\nFREE DOLLAR CHECK EXECUTED")
    soup = BeautifulSoup(response.content, "lxml")
    buy, sell = (float(tag.string.removeprefix("$")) for tag in soup.select(".value"))
    logger.warning(f"Buy: {buy} | Sell: {sell}\n")
    return buy, sell


class DollarScrapper:
    def __init__(self) -> None:
        response = get(url)
        self.soup = BeautifulSoup(response.content, "lxml")
        buy, sell = (float(tag.string.removeprefix("$")) for tag in self.soup.select(".value"))

    def get_free():
        logger.warning("\nFREE DOLLAR CHECK EXECUTED")

    def get_official():
        logger.warning("\nOFFICIAL DOLLAR CHECK EXECUTED")
