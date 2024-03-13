import logging
import requests

from core.models import DollarType

from core.connectors.dollar_recuiter import DollarRecruiter

logger = logging.getLogger(__name__)


class MEPDollarRecruiter(DollarRecruiter):
    def __init__(self) -> None:
        """
            Calculates the buying and selling prices for the MEP dollar from the web COnvert this request into a method
        """

        super().__init__()
        self.type_of_quote = DollarType.MEP.value
        self.url = "https://open.bymadata.com.ar/vanoms-be-core/rest/api/bymadata/free/bnown/seriesHistoricas/iamc/bonos"
        self.data = {"page_number": 1}
        self.al30, self.al30D = self.get_bond_prices()
        self.al30_buying_price = self.al30[0].get("cotizacion", None)
        self.al30d_selling_price = self.al30D[0].get("cotizacion", None)

        self.buying_price = self.al30_buying_price / self.al30d_selling_price
        self.selling_price = self.buying_price

    def get_bond_prices(self) -> tuple[dict]:
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
        # Process the JSON data
        data = response.json()
        list_bonds = data["data"]

        al30 = [bond for bond in list_bonds if bond.get("symbol", None) == "AL30"]
        al30D = [bond for bond in list_bonds if bond.get("symbol", None) == "AL30D"]

        return al30, al30D
