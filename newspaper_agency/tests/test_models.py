from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper_agency.models import Topic, Newspaper


class ModelTests(TestCase):

    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_name")

        self.assertEquals(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test123",
            password="password123",
            first_name="test_first",
            last_name="test_last",
            years_of_experience=10
        )

        self.assertEquals(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="test_name")

        newspaper = Newspaper.objects.create(
            title="tests",
            context="tests context",
            topic=topic,
        )

        self.assertEquals(
            str(newspaper),
            f"{newspaper.title} {newspaper.context} {newspaper.topic}"
        )
