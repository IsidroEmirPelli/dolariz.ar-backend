from core.models import Dollar
from django_filters.rest_framework import (
    DateTimeFilter,
    FilterSet,
    NumberFilter
)


class DollarFilterSet(FilterSet):
    """
    FilterSet for the Dollar model.

    Attributes:
    - type_of_quote (str): Dollar quotation.
    - date_from (DateTimeFilter): "From" date and time of the dollar.
    - date_to (DateTimeFilter): "To" date and time of the dollar.
    """

    type_of_quote = NumberFilter(
        field_name="type_of_quote",
        help_text="Dollar quotation",
    )
    date_from = DateTimeFilter(
        field_name="date",
        help_text='"From" date and time of the dollar',
    )
    date_to = DateTimeFilter(
        field_name="date",
        help_text='"To" date and time of the dollar',
    )

    class Meta:
        model = Dollar
        fields = ["date"]
