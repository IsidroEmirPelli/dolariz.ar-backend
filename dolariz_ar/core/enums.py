from django.utils.translation import gettext_lazy as _
from django_enumfield import enum


class DolarType(enum.Enum):
    OFICIAL = 1
    BLUE = 2
    MEP = 3
    CCL = 4
    LEDES = 5

    __labels__ = {
        OFICIAL: _("Oficial"),
        BLUE: _("Blue"),
        MEP: _("MEP"),
        CCL: _("CCL"),
        LEDES: _("Ledes")
    }
