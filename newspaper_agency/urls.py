from django.urls import path

from newspaper_agency.views import (
    index,
    TopicListView,
    TopicCreatedView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreatedView,
    RedactorYearOfExperienceUpdateView,
    RedactorDeleteUpdateView,
    NewspapersListView,
    NewspapersDetailView,
    NewspapersCreateView,
    NewspapersUpdateView,
    NewspapersDeleteView
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
    path(
        "redactors/create/",
        RedactorCreatedView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorYearOfExperienceUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteUpdateView.as_view(),
        name="redactor-delete"
    ),
    path(
        "newspapers/",
        NewspapersListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers/<int:pk>/detail/",
        NewspapersDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspapers/create/",
        NewspapersCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspapersUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspapersDeleteView.as_view(),
        name="newspaper-delete"
    ),
]

app_name = "newspaper_agency"
