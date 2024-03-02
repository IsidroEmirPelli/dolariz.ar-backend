import logging

from bs4 import BeautifulSoup
from requests import get

from constants import (
    BLUE_DOLLAR_URL as blue_url,
    OFFICIAL_DOLLAR_URL as official_url,
)

from .celery import app

logger = logging.getLogger(__name__)


@app.task
def get_blue() -> tuple[float, float]:
    """
    Get the official prices for buying and selling dollars on the web.

    Returns:
    - buying_price (float): blue dollar buy price.
    - selling_price (float): blue dollar sell price.
    """

    soup = (
        BeautifulSoup(get(blue_url).content, "lxml")
        .find("section", class_="modulo__cotizaciones")
        .find("a", string="Dólar blue")
        .parent
    )
    buying_price = (
        soup.find("div", class_="compra")
        .find("div", class_="val")
        .string.removeprefix("$")
    )
    selling_price = (
        soup.find("div", class_="venta")
        .find("div", class_="val")
        .string.removeprefix("$")
    )

    return buying_price, selling_price


@app.task
def get_official() -> tuple[float, float]:
    """
    Get the official prices for buying and selling dollars on the web.

    Returns:
    - buying_price (float): official dollar buy price.
    - selling_price (float): official dollar sell price.
    """

    soup = (
        BeautifulSoup(get(official_url).content, "lxml")
        .find("div", id="divisas")
        .find(string="Dolar U.S.A")
        .parent.parent.find_all("td")[1:]
    )
    buying_price = float(soup[0].string)
    selling_price = float(soup[1].string)
    return buying_price, selling_price
