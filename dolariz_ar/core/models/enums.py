from django.utils.translation import gettext_lazy as _
from django_enumfield.enum import Enum


class DollarType(Enum):
    OFFICIAL = 1
    BLUE = 2
    MEP = 3
    CCL = 4
    LEDES = 5

    __labels__ = {
        OFFICIAL: _("Official"),
        BLUE: _("Blue"),
        MEP: _("MEP"),
        CCL: _("CCL"),
        LEDES: _("Ledes")
    }
