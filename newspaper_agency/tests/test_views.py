from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper_agency.models import Newspaper, Topic

TOPIC_URL = reverse("newspaper_agency:topic-list")
NEWSPAPER_URL = reverse("newspaper_agency:newspaper-list")
REDACTOR_URL = reverse("newspaper_agency:redactor-list")


class PrivateTopicTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tests",
            password="password123",
            years_of_experience=10
        )
        self.client.force_login(self.user)

    @staticmethod
    def create_test_data():
        number_of_topics = 8

        for topic_id in range(number_of_topics):
            Topic.objects.create(name=f"name {topic_id}")

    def test_view_url_exist_at_needed_location(self):
        response = self.client.get(TOPIC_URL)

        self.assertEquals(response.status_code, 200)

    def test_pagination_is_5(self):
        self.create_test_data()
        response = self.client.get(TOPIC_URL)

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["topic_list"]), 5)

    def test_correct_template_used(self):
        response = self.client.get(TOPIC_URL)

        self.assertTemplateUsed(response, "newspaper_agency/topic_list.html")

    def test_list_all_topic(self):
        self.create_test_data()
        response = self.client.get(TOPIC_URL + "?page=2")

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["topic_list"]), 3)

    def test_search_topic_by_name(self):
        Topic.objects.create(name="name")
        search_name = "name"
        response = self.client.get(
            TOPIC_URL, {"name": search_name}
        )

        self.assertEquals(response.status_code, 200)
        topic_in_context = Topic.objects.filter(
            name__icontains=search_name
        )

        self.assertQuerysetEqual(
            response.context["topic_list"],
            topic_in_context
        )


class PublicTopicListViewTests(TestCase):

    def test_topic_login_required(self):
        response = self.client.get(TOPIC_URL)

        self.assertNotEquals(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(TOPIC_URL)

        self.assertRedirects(response, "/accounts/login/?next=/topics/")


class PrivateNewspaperTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_name",
            password="test_password",
            years_of_experience=10
        )
        self.client.force_login(self.user)

    @staticmethod
    def crate_test_data():
        topic = Topic.objects.create(name="name")

        number_of_newspapers = 8

        for newspaper_id in range(number_of_newspapers):
            Newspaper.objects.create(
                title=f"tests{newspaper_id}",
                context="test_context",
                topic=topic,
            )

    def test_view_url_exist_at_needed_location(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertEquals(response.status_code, 200)

    def test_pagination_is_5(self):
        self.crate_test_data()
        response = self.client.get(NEWSPAPER_URL)

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["newspaper_list"]), 5)

    def test_correct_template_used(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertTemplateUsed(response, "newspaper_agency/newspaper_list.html")

    def test_list_all_newspapers(self):
        self.crate_test_data()
        response = self.client.get(NEWSPAPER_URL + "?page=2")

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["newspaper_list"]), 3)

    def test_search_car_by_title(self):
        topic = Topic.objects.create(name="name")
        Newspaper.objects.create(
            title="tests",
            context="tests context",
            topic=topic,
        )
        search_model = "tests"
        response = self.client.get(
            NEWSPAPER_URL, {"model": search_model}
        )

        self.assertEquals(response.status_code, 200)
        newspaper_in_contest = Newspaper.objects.filter(
            title__icontains=search_model
        )

        self.assertQuerysetEqual(
            response.context["newspaper_list"],
            newspaper_in_contest
        )


class PublicNewspaperTests(TestCase):

    def test_newspaper_login_required(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertNotEquals(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertRedirects(response, "/accounts/login/?next=/newspapers/")


class PrivateRedactorTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_name",
            password="password123",
            years_of_experience=10

        )
        self.client.force_login(self.user)

    @staticmethod
    def create_test_data():
        number_od_redactors = 8

        for redactor_id in range(number_od_redactors):
            get_user_model().objects.create_user(
                username=f"test_name{redactor_id}",
                password=f"password123{redactor_id}",
                years_of_experience=10

            )

    def test_view_url_exist_at_needed_location(self):
        response = self.client.get(REDACTOR_URL)

        self.assertEquals(response.status_code, 200)

    def test_pagination_is_5(self):
        self.create_test_data()
        response = self.client.get(REDACTOR_URL)

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["redactor_list"]), 3)

    def test_correct_template_used(self):
        response = self.client.get(REDACTOR_URL)

        self.assertTemplateUsed(response, "newspaper_agency/redactor_list.html")

    def test_list_all_redactors(self):
        self.create_test_data()
        response = self.client.get(REDACTOR_URL + "?page=2")

        self.assertEquals(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEquals(len(response.context["redactor_list"]), 3)

    def test_search_redactor_by_username(self):
        get_user_model().objects.create_user(
            username="test_name2",
            password="password1223",
            years_of_experience=10
        )
        search_username = "test_name2"
        response = self.client.get(
            REDACTOR_URL, {"username": search_username}
        )

        self.assertEquals(response.status_code, 200)
        redactor_in_context = get_user_model().objects.filter(
            username__icontains=search_username
        )

        self.assertQuerysetEqual(
            response.context["redactor_list"],
            redactor_in_context
        )


class PublicDriverTests(TestCase):

    def test_redactor_login_required(self):
        response = self.client.get(REDACTOR_URL)

        self.assertNotEquals(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(REDACTOR_URL)

        self.assertRedirects(response, "/accounts/login/?next=/redactors/")
