from django.urls import path

from newspaper_agency.views import (
    index,
    TopicListView,
    TopicCreatedView,
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
    path(
        "topics/create/",
        TopicCreatedView.as_view(),
        name="topic-create"
    ),
]

app_name = "newspaper_agency"
