from core.models import Dollar
from django_filters.rest_framework import DateTimeFilter, FilterSet


class DollarFilterSet(FilterSet):
    """
    FilterSet for the Dollar model.

    Attributes:
    - date_from (DateTimeFilter): "From" date and time of the dollar.
    - date_to (DateTimeFilter): "To" date and time of the dollar.
    """

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
