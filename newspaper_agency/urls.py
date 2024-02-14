from django.urls import path

from newspaper_agency.views import (
    index,
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    )
]

app_name = "newspaper_agency"
