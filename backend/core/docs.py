from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Skillfolio-API",
        default_version='v1',
        description="Backend API for Skillfolio",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="Kanan Niftiyev"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)