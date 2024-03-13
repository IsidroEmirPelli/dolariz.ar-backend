import logging

from core.models import Dollar, DollarType
from core.serializers import DollarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import DollarFilterSet
from .services import get_dollar_price_by_type_of_quote_from_cache, get_dollar_prices_from_cache
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

logger = logging.getLogger(__name__)


class DollarViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for the Dollar model that allows to list and retrieve the dollar prices.
    """

    queryset = Dollar.objects.all()
    serializer_class = DollarSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = DollarFilterSet
    ordering_fields = ["price_buy", "price_sell", "date"]

    @extend_schema(
        summary='Cotización del dólar',
        description='Obtener el precio y variación del dólar según el tipo de cotización.',
        parameters=[
            OpenApiParameter(
                "type_of_quote",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description='Tipo de cotización',
            ),
        ],
        tags=['Cotización', ]
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="single",
        url_name="single"
    )
    def single(self, request, *args, **kwargs):
        """
        Obtain the dollar price from cache if available, else from db.
        """

        query_params = request.query_params.get("type_of_quote", None)
        if query_params:
            type_of_quote = query_params[0]
        if not query_params or int(type_of_quote) not in DollarType.__labels__.keys():
            logger.info(f"{self.__class__.__name__} obtain_price → UNSUCCESS.")
            return Response(
                {"message": "Tipo de cotización inválido."},
                status=HTTP_400_BAD_REQUEST,
            )
        data = get_dollar_price_by_type_of_quote_from_cache(type_of_quote)
        logger.info(f"{self.__class__.__name__} obtain_price → SUCCESS.")
        return Response(data, status=HTTP_200_OK)

    @action(
        detail=False,
        methods=["get"],
        url_path="multiple",
        url_name="multiple"
    )
    def multiple(self, request, *args, **kwargs):
        """
        Obtain the dollar prices from cache if available, else from db.
        """

        dollars = get_dollar_prices_from_cache()
        logger.info(f"{self.__class__.__name__} obtain_price → SUCCESS.")
        return Response(dollars, status=HTTP_200_OK)
