import logging
import requests

from dolariz_ar.core.connectors.dollar_recruiter import DollarRecruiter

logger = logging.getLogger(__name__)


class DollarRecruiterByma(DollarRecruiter):
    def __init__(self) -> None:
        """
        Calculates the buying and selling prices for the MEP dollar from the web COnvert this request into a method
        """

        super().__init__()
        self.bond, self.bondD = self.get_bond_prices(
            self.bond_value,
            self.bondD_value,
        )

        (
            self.bond_buying_price,
            self.bondD_selling_price,
        ) = self.get_prices_from_response()

        self.buying_price = self.bond_buying_price / self.bondD_selling_price
        self.selling_price = self.buying_price

    def get_prices_from_response(self) -> tuple[float]:
        """
        Get the buying and selling prices from the response of the web.

        Returns
        -------
        tuple[float]
            The buying and selling prices.
        """

        bond_buying_price = self.bond[0].get("cotizacion", None)
        bondD_selling_price = self.bondD[0].get("cotizacion", None)

        return bond_buying_price, bondD_selling_price

    def get_bond_prices(self, bond_value, bondD_value) -> tuple[dict]:
        """
        Get the prices of the bonds from the web.

            This return something like this
        (
            {
                "descripcion":"BONO NACIÓN ARG. U$S STEP UP LEY ARG. VTO. 9/7/2030",
                "symbol":"AL30",
                "hora":"01:25",
                "notas":"",
                "paridad":0.48038,
                "fechaCot":"2024-03-13",
                "dm":2.2921,
                "tirAnual":0.289431,
                "cotizacion":49385,
                "vTecnico":100.135417,
                "vr":100,
                "intCorr":0.135417,
                "rentaAnual":"Fija=0.75",
                "isin":"ARARGE3209S6"
            },
            {...}
        )
        """

        response = requests.post(self.url, json=self.data, verify=False)

        # Check for successful response
        if response.status_code != 200:
            logger.error(f"Error: {response.status_code} {response.text}")
            return []

        data = response.json()
        list_bonds = data["data"]

        bond = [bond for bond in list_bonds if bond.get("symbol", None) == bond_value]
        bondD = [bond for bond in list_bonds if bond.get("symbol", None) == bondD_value]

        return bond, bondD
