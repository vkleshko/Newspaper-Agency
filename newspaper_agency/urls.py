from django.urls import path

from newspaper_agency.views import (
    index,
    TopicListView,
    TopicCreatedView,
    TopicUpdateView,
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
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
]

app_name = "newspaper_agency"
