from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from .views import CachedDollarAPIView, DollarViewSet

router = DefaultRouter()

router.register(r"dollar", DollarViewSet, basename="dollar")

urlpatterns = [
    path("cached/<str:type_of_quote>/", CachedDollarAPIView.as_view(), name="cached"),
    path("", include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
