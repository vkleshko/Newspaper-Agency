from django.urls import path

from newspaper_agency.views import (
    index,
    TopicListView,
    TopicCreatedView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
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
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
]

app_name = "newspaper_agency"
