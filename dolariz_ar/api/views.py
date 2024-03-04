import logging

from core.models import Dollar, DollarType
from core.serializers import CacheDollarSerializer, DollarSerializer
from core.services import get_official_dollar_prices_and_variations_from_cache_service
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    # HTTP_404_NOT_FOUND,
)

from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import DollarFilterSet

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

    # CONSULTAR lookup_field CON ISIDRO Y REFERENCIAR EL SERIALIZER
    # lookup_field = "date"

    def list(self, request, *args, **kwargs):
        """
        List the dollar prices.
        """

        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            logger.info(f"{self.__class__.__name__} list -> SUCCESS")
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logger.error(
                f"{self.__class__.__name__} list -> Error listing the dollar prices: {e}"
            )
            return Response(
                {"message": "Error al enlistar los precios"},
                status=HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a dollar price.
        """

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            logger.info(f"{self.__class__.__name__} retrieve -> SUCCESS")
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logger.error(
                f"{self.__class__.__name__} retrieve -> Error retrieving the dollar price: {e}"
            )
            return Response(
                {"message": "Error al obtener el precio del dolar-"},
                status=HTTP_400_BAD_REQUEST,
            )


class CachedDollarAPIView(APIView):
    """
    APIView for the cached dollar that allows to obtain their prices and variations.
    """

    def get(self, request, type_of_quote: DollarType) -> Response:
        """
        Get the cached dollar prices and variations.
        """

        data = get_official_dollar_prices_and_variations_from_cache_service(
            type_of_quote
        )
        serializer = CacheDollarSerializer(data=data)
        serializer.is_valid()
        logger.info(f"{self.__class__.__name__} get -> SUCCESS")
        return Response(serializer.data)
