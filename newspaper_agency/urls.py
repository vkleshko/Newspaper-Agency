from django.urls import path

from newspaper_agency.views import (
    index,
    TopicListView
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),
]

app_name = "newspaper_agency"
