from django.urls import path

from bias_core.api.runtime import build_api_application
from bias_core.extensions.bootstrap import get_extension_host


api = build_api_application(extension_host=get_extension_host())

urlpatterns = [
    path("api/", api.urls),
]
